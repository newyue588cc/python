#!/usr/bin/python
#describe:smtplib_sendmail.py

import smtplib
import email.utils
from email.mime.text import MIMEText

#Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient','mark.li@buzzinate.com'))
msg['From'] = email.utils.formataddr(('Author','LYJ_216@126.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP()
server.connect("smtp.126.com")
server.login("LYJ_216","liyuejing@216")
server.set_debuglevel(True) #show communication with the server
try:
    server.sendmail('LYJ_216@126.com',['mark.li@buzzinate.com'],msg.as_string())
finally:
    server.quit()

