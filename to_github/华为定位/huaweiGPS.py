import time
from selenium import webdriver
from datetime import datetime
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
import sys
sys.path.append("c:\\")
from key import k

my_sender = "vc616@qq.com"  # 发件人邮箱账号
my_pass = k.email_pass  # 发件人邮箱密码
my_user = [k.my_sender , ]  # 收件人邮箱账号
import time
n = "zjn"
# n = "cvc"
sendtime = [0,30]

if os.path.exists( 'c:\\screenshot' ) == False: 
    os.makedirs( 'c:\\screenshot' )


def dwhua(shoujihao,m,key):
    browser = webdriver.Chrome()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    path = "C:/screenshot/" + m +"-" +current_time + ".png"
    print(current_time,path)
    try:

        browser.get("https://cloud.huawei.com/")
        
        # browser.maximize_window()
        time.sleep(3)
        browser.set_window_size(1400,1060)
        browser.switch_to.frame("frameAddress")
        browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[1]/form/div[3]/div/div/div/input").send_keys(shoujihao)
        browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[1]/form/div[4]/div/div/div/input").send_keys(key)
        # time.sleep(3)
        browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[1]/div/div/div").click()
        time.sleep(3)
        try:
            browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[5]/div[2]/div[2]/div[1]").click()
            time.sleep(1) 
        except:
            pass

        browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[9]/div/div/div[6]/div[1]/div").click()
        time.sleep(3)
        # print("1")
        # browser.maximize_window()
        s1 = 1
        t1 = 0
        s2 = ""
        while(s1 == 1):
            try:
                s2 = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[6]/div[2]/div[1]/div[2]/span[1]").text
                print(s2)                
            except:
                pass
                
            if (t1 > 30):
                break
            if s2 == "刚刚更新" :
                try:              
                    ard = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[6]/div[2]/div[1]/div[1]").text
                                                #  /html/body/div[1]/div[6]/div[6]/div[2]/div[1]/div[1]
                except:
                    ard = "读取网页信息错误"
                try:            
                    wifi = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[6]/div[2]/div[1]/div[3]/div[2]/div/span[2]").text
                                                        #   /html/body/div[1]/div[6]/div[6]/div[2]/div[1]/div[3]/div[2]/div/span[2]                                                    
                except:
                    wifi = "无"
                try:
                    dianliang = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[6]/div[2]/div[1]/div[3]/div[1]/div/div/div[2]").text        
                except:            
                    dianliang = "无"
                break
            t1 = t1 + 1
            time.sleep(1)
            print("等待定位：",t1)
        # print("2")
        browser.save_screenshot(path)
        if ard == "":
            ard = "读取网页信息错误"
            wifi = "无"
            dianliang = "无"
        print("地址：",ard,"wifi：",wifi,"电量：",dianliang)
        s = ard.find("市") + 1
        w = ard[0:s]
        title =  m +"（" + w + "）"
        current_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        text = "<p>地址：" + ard + "</p>\r\n  <p>wifi：" + wifi + "</p>\r\n<p>电量：" + dianliang +"<p>\r\n<p>时间：" + current_time1 +"<p>"
        browser.quit()
        return [title,text,path,ard]
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("定位失败")
        return["网页打开失败","网页打开失败","网页打开失败","网页打开失败"]   


def dwmi(shoujihao,m,key):
    browser = webdriver.Chrome()
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    path = "C:/screenshot/" + m +"-" +current_time + ".png"
    print(current_time,path)
    try:
        browser.get("https://account.xiaomi.com/fe/service/login/password?_snsNone=true&_locale=zh_CN&sid=i.mi.com&qs=%253Fcallback%253Dhttps%25253A%25252F%25252Fi.mi.com%25252Fsts%25253Fsign%25253DmF32YtfY7XReThOa0pZzXhZXJ0U%2525253D%252526followup%25253Dhttps%2525253A%2525252F%2525252Fi.mi.com%2525252F%252526sid%25253Di.mi.com%2526sid%253Di.mi.com%2526_locale%253Dzh_CN%2526_snsNone%253Dtrue&callback=https%3A%2F%2Fi.mi.com%2Fsts%3Fsign%3DmF32YtfY7XReThOa0pZzXhZXJ0U%253D%26followup%3Dhttps%253A%252F%252Fi.mi.com%252F%26sid%3Di.mi.com&_sign=9jXUgB%2FpG9gyrojgrYozJpnskkE%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=")

        time.sleep(3)
        # browser.maximize_window()vc
        # browser.switch_to.frame("frameAddress")
        browser.find_element_by_name("account").send_keys(shoujihao)
        browser.find_element_by_name("password").send_keys(key)
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/form/div/button").click()
        time.sleep(3)
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/a[7]/div[1]").click()
        time.sleep(3)
        
        browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]").click()
        time.sleep(60)
        # browser.maximize_window()
        # ard = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[5]/div[2]/div[1]/div[1]").text
        # wifi = browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[5]/div[2]/div[1]/div[3]/div[2]/div/span[2]").text
        dianliang = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]").text
        browser.save_screenshot(path)
        ard = "null"
        wifi = "null"
        print("地址：",ard,"wifi：",wifi,"电量：",dianliang)
        s = ard.find("市") + 1
        w = ard[0:s]
        title =  m +"（" + w + "）"
        text = "<p>地址：" + ard + "</p>\r\n  <p>wifi：" + wifi + "</p>\r\n<p>电量：" + dianliang +"<p>"
        browser.quit()
        return [title,text,path,ard]
        print("定位成功")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("定位失败")
        return["","","",""]   

def email(st):
    
    msg = MIMEMultipart('related')
    # msg['From'] = Header("vc616@qq.com", 'utf-8')
    msg["From"] = formataddr(["vc",my_sender])
    # msg['To'] =  Header("vc616@qq.com", 'utf-8')
    msg["To"] = formataddr(["vc",my_sender])

    subject = "GPS"
    msg['Subject'] = Header(subject, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    t = 1
    mail_msg = ""
    for i in st:
        mail_msg = mail_msg + i[1] + """\r\n<p><img src="cid:image"""+ str(t) + """"></p>\r\n"""
        t= t+1
    print(mail_msg)
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    t = 1
    for i in st:
        try:
            print(i[2])
            fp = open(i[2], 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()        
            msgImage.add_header('Content-ID', "<image"+ str(t) +">")
            msg.attach(msgImage)
        except:
            pass
        t = t +1
    return(msg)


def send(msg):
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("邮件发送失败")
 

    
l = []
m = 0
while 1:
    localtime = time.localtime(time.time())
    s = []
    r = []
    if (localtime.tm_min  in sendtime) :
        # s.append(dwhua(k.nova8,"Nova 8",k.nova8_pass))
        # print(s)
        # time.sleep(60)
        
        s.append(dwhua(k.mate40_phone,"Mate 40",k.mate40_pass))
        # print(s)
        # email(s)
        # s.append(dwmi(k.mi9_phone,"Mi9"，k.mi9_pass))
        # s.append(dwmi(k.mi8_phone,"Mi8",k.mi8_pass))
        r = s[:]
        if l == []:
            send(email(s))
            m = 0
            l =  r[:] 
        else:
            for i in range(len(l)):
                if l[i][3] != s[i][3]:
                    m = 1
                    s.append(l[i])
            if m == 1:
                send(email(s))
                m = 0
                l =  r[:] 
            else:
                print("位置未更改")
        


    else:
        print(localtime.tm_hour,":",localtime.tm_min)
    time.sleep(10)



