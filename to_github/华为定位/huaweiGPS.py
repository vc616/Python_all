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

my_sender = "vc616@qq.com"  # 发件人邮箱账号
my_pass = "mtnvaffnymivbjif"  # 发件人邮箱密码
my_user = ["vc616@qq.com", ]  # 收件人邮箱账号
import time
n = "zjn"
# n = "cvc"
sendtime = [0,15,30,45]

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
        browser.find_element_by_id("login_userName").send_keys(shoujihao)
        browser.find_element_by_id("login_password").send_keys(key)
        time.sleep(1)
        browser.find_element_by_id("btnLogin").click()
        time.sleep(3)
        browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[9]/div/div/div[6]/div[1]/div").click()
        time.sleep(30)
        # print("1")
        # browser.maximize_window()
        try:
            ard = browser.find_element_by_xpath("/html/body/div[1]/div[5]/div[6]/div[2]/div[1]/div[1]").text
        except:
            ard = "读取网页信息错误"
        try:            
            wifi = browser.find_element_by_xpath("/html/body/div[1]/div[5]/div[6]/div[2]/div[1]/div[3]/div[2]/div/span[2]").text
                                                 
        except:
            wifi = "无"
        try:
            dianliang = browser.find_element_by_xpath("/html/body/div[1]/div[5]/div[6]/div[2]/div[1]/div[3]/div[1]/div/div/div[2]").text
       
        except:            
            dianliang = "无"
        # print("2")
        browser.save_screenshot(path)
        
        print("地址：",ard,"wifi：",wifi,"电量：",dianliang)
        s = ard.find("市") + 1
        w = ard[0:s]
        title =  m +"（" + w + "）"
        text = "<p>地址：" + ard + "</p>\r\n  <p>wifi：" + wifi + "</p>\r\n<p>电量：" + dianliang +"<p>"
        browser.quit()
        return [title,text,path,ard]
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("定位失败")
        return["","","",""]   


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
    msg['From'] = Header("vc616@qq.com", 'utf-8')
    msg['To'] =  Header("vc616@qq.com", 'utf-8')
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
    if (localtime.tm_min in sendtime) :
        # s.append(dwhua("13466648179","Nova 8","160218vc"))
        # print(s)
        # time.sleep(60)
        s.append(dwhua("18811505321","Mate 40","160218cvcAzjn"))
        # print(s)
        # s = [['Nova 8（北京市）', '<p>地址：北京市大兴区北京经济技术开发区朝林大厦A座朝林广场</p>\r\n  <p>wifi：LINK66_5G</p>\r\n<p>电量：100%<p>', 'C:/Users/VM/Desktop/screenshot/Nova 8-2021-09-13-11_44_02.png'], ['Mate 40（北京市）', '<p>地址：北京市大兴区北京经济技术开发区北京</p>\r\n  <p>wifi：OFFICE 5G</p>\r\n<p>电量：42%<p>', 'C:/Users/VM/Desktop/screenshot/Mate 40-2021-09-13-11_44_48.png']] 
        # email(s)
        # s.append(dwmi("13466648179","Mi9","160218cvcAzjn"))
        # s.append(dwmi("13582388147","Mi8","160218cvcAzjn"))
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
    time.sleep(30)



