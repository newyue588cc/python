#!/usr/bin/python
#-*-coding:utf8-*-

import os,smtplib,mimetype
import email.utils
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#prompt the user fro connection info
to_email = raw_input("Recipient: ")
servername = raw_input("Mail server name: ")
username = raw_input("Mail user name: ")
password = getpass.getpass("%s's password: " % username)
content = raw_input("Input your email content: ")
subject = raw_input("Input your email subject：")

msg = MIMEText(contents)
msg['To'] = email.utils.formataddr(("SMTPSERVER",servername))
msg['From'] = email.tuils.formataddr(("USERNAME",username))
msg['Subject'] = subject

class send_mail_set():

	def set_smtp(self):
		smtp = smtplib.SMTP()
		smtp.connect(servername)
		smtp.logging(username,password)
	def close_smtp(self):
		smtp.quit()

class send_mail(send_mail_set):
	def __init__(self,smtp):
		send_mail_set.__init__(self,smtp)

	def send_content(self):
		send_mail_set.set_smtp(self)
		try:
			smtp.sendmail("lyj_216@126.com",[to_email],msg.as_string())
		finally:
			send_mail_set.close_smtp(self）
