#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr
from email.utils import formataddr
from email.header import Header
 
 
def __format_addr__(addr):
 # 解析邮件地址，以保证邮有别名可以显示
    alias_name, addr = parseaddr(addr)
 # 防止中文问题，进行转码处理，并格式化为str返回
    return formataddr((Header(alias_name,charset="utf-8").encode(),addr.encode("uft-8") if isinstance(addr, unicode) else addr))
 
 
def send_email_to(fromAdd, toAdd, subject, html_text, filename=None):

    SERVER = 'mail.***.com'
    USER = '******'
    PASSWD = '***'
 
    strFrom = __format_addr(fromAdd)
 
    strTo = list()
    # 原来是一个纯邮箱的list，现在如果是一个["jayzhen<jayzhen@jz.com>"]的list给他格式化
    try:
        for a in toAdd:
            strTo.append(__format_addr(a))
    except Exception as e:
        # 没有对a和toadd进行type判断，出错就直接还原
        strTo = toAdd

msgRoot = MIMEMultipart('related')
msgRoot.preamble = 'This is a multi-part message in MIME format.'
 
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
 
 # 邮件对象 
html_text = "用来测试的邮件文本"
msgText = MIMEText(html_text, 'html', 'utf-8')
msgRoot['Subject'] = Header("菜鸟教程", 'utf-8') # 这是邮件的主题，通过Header来标准化
msgRoot['From'] = strFrom  # 发件人也是被格式化过的
msgRoot['to'] = ','.join(strTo) # 这个一定要是一个str,不然会报错“AttributeError: 'list' object has no attribute 'lstrip'”
msgAlternative.attach(msgText)

smtp = smtplib.SMTP(SERVER, 11)
smtp.set_debuglevel(0)
 # smtp.connect(SERVER)
smtp.login(USER, PASSWD)
 # 这里要注意了，这里的fromadd和toAdd和msgRoot['From'] msgRoot['to']的区别
smtp.sendmail(fromAdd, toAdd, msgRoot.as_string())
smtp.quit()