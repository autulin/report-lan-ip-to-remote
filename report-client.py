#!/usr/bin/python
#-*-coding:utf8-*-

import socket
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests
import datetime

url = "http://your-server/ip"

### edit your SMTP email config
smtpserver = "smtp.xxx.com"
username = "your username"
password = "your password"
sender = "user@xxx.com"
receiver = ["receiver@xxx.com"]
subject = "edit your email subject"

def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr

def sendEmail(msg):
    msgRoot = MIMEMultipart('related')
    msgRoot["To"] = ','.join(receiver)
    msgRoot["From"] = sender
    msgRoot['Subject'] = subject
    msgText = MIMEText(msg,'html','utf-8')
    msgRoot.attach(msgText)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

def report(url, ip, isSendMail=False):
    response = requests.post(url, json={"ip": ip})
    if response.status_code == requests.codes.ok:
        print("[%s]report success!(%s)" % (datetime.datetime.now(), ip))
    else:
        print("[%s]report failed." % datetime.datetime.now())
        print(response.text)
    if isSendMail:
        sendEmail(ip)
        print("[%s]send mail success!" % datetime.datetime.now())

def get_and_send():
    last_ip = ''
    while True:
        try:
            lan_ip = get_lan_ip()
            if lan_ip != last_ip:
                report(url, lan_ip)
        except Exception as e:
            last_ip = ''
            print(e)
        time.sleep(10000)
    
if __name__ == '__main__':
    get_and_send()