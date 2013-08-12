#!/usr/bin/python

import smtplib

server = smtplib.SMTP()
server.connect("smtp.126.com")
server.login("LYJ_216","liyuejing@216")
server.set_debuglevel(True)
try:
    dhellmann_result = server.verify('LYJ_216@126.com')
    notthere_result = server.verify('123454@126.com')
finally:
    server.quit()

print 'LYJ_216:',dhellmann_result
print 'notthere:',notthere_result
