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
        browser.find_element_by_id("login_userName").send_keys(shoujihao)
        browser.find_element_by_id("login_password").send_keys(key)
        time.sleep(1)
        browser.find_element_by_id("btnLogin").click()
        time.sleep(3)
        browser.find_element_by_xpath("/html/body/div[1]/div[6]/div[9]/div/div/div[6]/div[1]/div").click()
        time.sleep(3)
        browser.get_log()



    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("定位失败")
        return["","","",""]   





