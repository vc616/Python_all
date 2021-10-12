#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from email import header
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header




import sys
sys.path.append("c:\\")
from key import k

my_sender='406086398@qq.com'    # 发件人邮箱账号
my_pass = k.email_pass             # 发件人邮箱密码
my_user='vc616@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    
    msg=MIMEText('填写邮件内容','plain','utf-8')
    msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="菜鸟教程发送邮件测试"               # 邮件的主题，也可以说是标题
    print(msg.as_string())
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    msgRoot = MIMEMultipart('related')
    # msgRoot['From'] = Header("406086398@qq.com", 'utf-8')
    msgRoot["From"] = formataddr(["FromRunoob",my_sender])
    # msgRoot['To'] =  Header("406086398@qq.com", 'utf-8')
    msgRoot['To'] =  formataddr(["FromRunoob",my_sender])
    subject = 'Python SMTP 邮件测试'
    msgRoot['Subject'] = Header(subject, 'utf-8')
    
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    
    
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
    print(msgRoot.as_string())





    server=smtplib.SMTP_SSL("smtp.qq.com", 465)       # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user,],msgRoot.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    
    return ret
 
ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")