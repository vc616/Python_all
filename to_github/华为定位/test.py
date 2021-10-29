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

browser = webdriver.Chrome()
browser.get("https://cloud.huawei.com/")
        
# browser.maximize_window()

time.sleep(3)
# browser.set_window_size(1400,1060)
browser.switch_to.frame("frameAddress")
browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[1]/form/div[3]/div/div/div/input").send_keys(shoujihao)
browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[1]/form/div[4]/div/div/div/input").send_keys(key)
time.sleep(1)
browser.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[1]/div/div/div").click()
                            #    /html/body/div/div[1]/div[4]/div[1]/div/div/div/div