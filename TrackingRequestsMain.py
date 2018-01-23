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

#Getting DB of requests to be checked
from ListOfRequests import *

TemplateBlock='  <tr>\n    <td>REQUEST</td>\n    <td style="color:Tomato;">STATUS</td>\n    <td>CONTACT</td>\n    <td>ANALYZER</td>\n    <td> <a href="https://cms-pdmv.cern.ch/mcm/requests?range=REQI,REQF">McM Link</a> </td>\n  </tr>\n'

FillingTable=''

for i in ListOfRequests:
    FillingTable=FillingTable+TemplateBlock.replace('REQUEST',i.Name).replace('CONTACT',i.Contact).replace('ANALYZER',i.Analyzer).replace('REQI',i.PrepIds[0]).replace('REQF',i.PrepIds[-1])
    print FillingTable

#cmd.getoutput('sed -i -- "s#FILLTABLEHERE#'+FillingTable+'#g" '+BaseDirectory+SiteName+'/index.html')
index_html=open(BaseDirectory+SiteName+'/index.html','r')
html_lines=index_html.readlines()
index_html.close()
html_lines[html_lines.index('FILLTABLEHERE\n')]=FillingTable
index_html=open(BaseDirectory+SiteName+'/index.html','w')
index_html.writelines(html_lines)
index_html.close()
