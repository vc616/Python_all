#!/usr/bin/env python
import RPi.GPIO as GPIO
import numpy as np
import time
import pymysql


DHTPIN = 21         #引脚号17

GPIO.setmode(GPIO.BCM)      #以BCM编码格式

def read_dht11_dat():
    
    GPIO.setup(DHTPIN, GPIO.OUT)
    GPIO.output(DHTPIN, GPIO.LOW)
    #给信号提示传感器开始工作,并保持低电平18ms以上
    time.sleep(0.02)                #这里保持20ms   
    GPIO.output(DHTPIN, GPIO.HIGH)  #然后输出高电平
    
    GPIO.setup(DHTPIN, GPIO.IN)    
    # 发送完开始信号后得把输出模式换成输入模式，不然信号线上电平始终被拉高
 
    while GPIO.input(DHTPIN) == GPIO.LOW:
        continue
    #DHT11发出应答信号，输出 80 微秒的低电平
    
    while GPIO.input(DHTPIN) == GPIO.HIGH:
        continue
    #紧接着输出 80 微秒的高电平通知外设准备接收数据
    
    
    #开始接收数据
    j = 0               #计数器
    data = []           #收到的二进制数据
    kk=[]               #存放每次高电平结束后的k值的列表
    while j < 40:
        k = 0
        while GPIO.input(DHTPIN) == GPIO.LOW:  # 先是 50 微秒的低电平
            continue
        
        while GPIO.input(DHTPIN) == GPIO.HIGH: # 接着是26-28微秒的高电平，或者 70 微秒的高电平
            k += 1
            if k > 100:
                break
        kk.append(k)
        if k < 8:       #26-28 微秒时高电平时通常k等于5或6
            data.append(0)      #在数据列表后面添加一位新的二进制数据“0”
        else:           #70 微秒时高电平时通常k等于17或18
            data.append(1)      #在数据列表后面添加一位新的二进制数据“1”
 
        j += 1
 
    #print("sensor is working.")
    #print('初始数据高低电平:\n',data)    #输出初始数据高低电平
    #print('参数k的列表内容：\n',kk )     #输出高电平结束后的k值
    
    m = np.logspace(7,0,8,base=2,dtype=int) #logspace()函数用于创建一个于等比数列的数组
    #即[128 64 32 16 8 4 2 1]，8位二进制数各位的权值
    data_array = np.array(data) #将data列表转换为数组

    #dot()函数对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)
    humidity = m.dot(data_array[0:8])           #用前8位二进制数据计算湿度的十进制值
    humidity_point = m.dot(data_array[8:16])
    temperature = m.dot(data_array[16:24])
    temperature_point = m.dot(data_array[24:32])
    check = m.dot(data_array[32:40])
    
    #print(humidity,humidity_point,temperature,temperature_point,check)
    
    tmp = humidity + humidity_point + temperature + temperature_point
    #十进制的数据相加
 
    if check == tmp:    #数据校验，相等则输出
        return humidity, temperature
    else:               #错误输出错误信息
        return False
 
def sql(h,t):

    db = pymysql.connect(host= '111.207.218.252', port= 8016, user= 'root', password= '160218vc',db = "test" )
    cursor = db.cursor()
    sq = """INSERT INTO test.温度 (temperature, humidity) VALUES( """ + t + """, """ + h + """)"""
    try:
        # 执行sql语句
        cursor.execute(sq)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()






def main():
    print("Raspberry Pi DHT11 Temperature test program\n")
    time.sleep(3)           #通电后前一秒状态不稳定，时延一秒
    avgh = 0
    avgt = 0
    sumh = 0
    sumt = 0
    t = 0

    while True:
        if int(time.time()) % 10 == 0:
            if t < 6:            
                result = read_dht11_dat()
                if result :
                    humidity, temperature = result
                    sumh = sumh + humidity
                    sumt = sumt + temperature
                    i = i +1
                if result == False:
                    print("Data are wrong,skip\n")                    
                t = t +1                
                if t == 5:
                    avgh = sumh / i
                    avgt = sumt / i
                    sql(avgh,avgt)
                    t = 0
        time.sleep(1)

            
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy() 
