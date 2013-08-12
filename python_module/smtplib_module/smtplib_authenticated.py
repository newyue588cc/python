#!/usr/bin/python
#-*-coding:utf8-*-

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

#prompt the user fro connection info
to_email = raw_input("Recipient: ")
servername = raw_input("Mail server name: ")
username = raw_input("Mail user name: ")
password = getpass.getpass("%s's password: " % username)

#create the message
msg = MIMEText("Test message from PyMOTW.")
msg.set_unixfrom('author')
msg["To"] = email.utils.formataddr(("Recipient",to_email))
msg["From"] = email.utils.formataddr(("Author","LYJ_216@126.com"))
msg['Subject'] = 'Test from PyMOTW'

server = smtplib.SMTP()
server.connect(servername)
try:
    server.set_debuglevel(True)
    server.ehlo()
    
    if server.has_extn("STARTTLS"):
        server.starttls()
        server.ehlo()

    server.login(username,password)
    server.sendmail(username + "@126.com"  ,[to_email],msg.as_string())
finally:
    server.quit()

