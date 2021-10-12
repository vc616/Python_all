#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import sys
sys.path.append("c:\\")
from key import k

my_sender = 'vc616@qq.com'
my_pass = k.email_pass
receivers = ['vc616@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("406086398@qq.com", 'utf-8')
msgRoot['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')
 
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
print(msgRoot)
 
 
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
# 指定图片为当前目录
fp = open('C:\\Users\\vm\\Documents\\python_all\\to_github\\email\\4.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
 
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
 
try:
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")