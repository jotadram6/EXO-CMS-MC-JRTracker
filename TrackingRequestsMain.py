#!/bin/python

DEBUG = False

import GetPassword #Safely parsing the username and password
import smtplib #Library to send email notifications
import commands as cmd
import time

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

#Setting working directory of the site
BaseDirectory='/afs/cern.ch/user/j/jruizalv/www/'
SiteName='JoseTestingEXO'

IsDirectoryThere=cmd.getoutput("ls "+BaseDirectory)
if SiteName in IsDirectoryThere:
    cmd.getoutput("cp -r PageSources/* "+BaseDirectory+SiteName+"/")
else:
    cmd.getoutput("cp -r PageSources "+BaseDirectory+SiteName)

print "Site created on: "+BaseDirectory+SiteName

ITime=time.localtime()
StringITime=str(ITime.tm_year)+'-'+str(ITime.tm_mon)+'-'+str(ITime.tm_mday)+' at '+str(ITime.tm_hour)+'h'+str(ITime.tm_min)+'m'

cmd.getoutput('sed -i -- "s/DATE/'+StringITime+'/g" '+BaseDirectory+SiteName+'/index.html')
