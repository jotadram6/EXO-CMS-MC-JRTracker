#!/bin/python

DEBUG = True

import GetPassword #Safely parsing the username and password
import smtplib #Library to send email notifications

#Getting username and password to send email notifications
LoginArgs=GetPassword.main(True)
User=LoginArgs.username
Password=LoginArgs.password.value

#Setting STMP
server = smtplib.SMTP('smtp.cern.ch', 587)
server.starttls()
server.login(User, Password)

if DEBUG:
    tolist=[User+"@cern.ch"]
    msg = 'From: jruizalv@cern.ch\nSubject: Hello World\n\nHello World!'
    server.sendmail(User+"@cern.ch", tolist, msg)
    print "Go check your email! A hello world email has been sent :)"
