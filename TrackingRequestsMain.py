#!/bin/python

DEBUG = False
DoNotify = True
TESTING = False
FromVM = True

if TESTING: DoNotify = False

import GetPassword #Safely parsing the username and password
import smtplib #Library to send email notifications
import commands as cmd
import time
import pandas as pd

if DEBUG:
    tolist=[User+"@cern.ch"]
    msg = 'From: jruizalv@cern.ch\nSubject: Hello World\n\nHello World!'
    server.sendmail(User+"@cern.ch", tolist, msg)
    print "Go check your email! A hello world email has been sent :)"

#Setting working directory of the site
if FromVM:
    BaseDirectory='/home/MonitoringEXOTools/HTML/'
else:
    BaseDirectory='/afs/cern.ch/user/j/jruizalv/www/'
if TESTING: 
    SiteName='Testing'
else:
    SiteName='EXO_MC_Monitoring'

#if FromVM: cmd.getoutput("mkdir -p "+BaseDirectory+SiteName)

IsDirectoryThere=cmd.getoutput("ls "+BaseDirectory)
if SiteName in IsDirectoryThere:
    cmd.getoutput("cp -r /home/MonitoringEXOTools/EXO-CMS-MC-JRTracker/PageSources/* "+BaseDirectory+SiteName+"/")
else:
    cmd.getoutput("cp -r /home/MonitoringEXOTools/EXO-CMS-MC-JRTracker/PageSources "+BaseDirectory+SiteName)

print "Site created on: "+BaseDirectory+SiteName

ITime=time.localtime()
StringITime=str(ITime.tm_year)+'-'+str(ITime.tm_mon)+'-'+str(ITime.tm_mday)+' at '+str(ITime.tm_hour)+'h'+str(ITime.tm_min)+'m'

cmd.getoutput('sed -i -- "s/DATE/'+StringITime+'/g" '+BaseDirectory+SiteName+'/index.html')

#Getting data structure
from DataStructure import *

#Getting DB of requests to be checked
from ListOfRequests import *

#Getting functions to fetch status
from GettingStatus import *

TemplateBlockDONE='  <tr>\n    <td>REQUEST</td>\n    <td>CAM</td>\n    <td style="color:#298A08;">STATUS</td>\n    <td>CONTACT</td>\n    <td>ANALYZER</td>\n    <td> <a href="https://cms-pdmv.cern.ch/mcm/requests?range=REQI,REQF">McM Link</a> </td>\n  </tr>\n'

TemplateBlockHALFDONE='  <tr>\n    <td>REQUEST</td>\n    <td>CAM</td>\n    <td style="color:#FF8000;">STATUS</td>\n    <td>CONTACT</td>\n    <td>ANALYZER</td>\n    <td> <a href="https://cms-pdmv.cern.ch/mcm/requests?range=REQI,REQF">McM Link</a> </td>\n  </tr>\n'

TemplateBlockSTUCK='  <tr>\n    <td>REQUEST</td>\n    <td>CAM</td>\n    <td style="color:Tomato;">STATUS</td>\n    <td>CONTACT</td>\n    <td>ANALYZER</td>\n    <td> <a href="https://cms-pdmv.cern.ch/mcm/requests?range=REQI,REQF">McM Link</a> </td>\n  </tr>\n'

FillingTable=''
df=pd.DataFrame()

kcounter=0

MessagesToBeSent=[]
EmailAddresses=[]

for i in ListOfRequests:
    if TESTING and kcounter>3: continue
    #FetchedMcMStatus='MCM: '+McMStatus(i.PrepIds) #Full string with status
    #FetchedMcMStatus='MCM: '+PercentageProdMcM(i.PrepIds)
    FetchedMcMStatus,df=PercentageProdMcM(i.PrepIds,df)
    FetchedMcMStatus='MCM: '+FetchedMcMStatus
    FetchedMcMCampaigns=McMCampaignSummary(i.PrepIds)
    #StringDONEinMCM=FetchedMcMStatus.split("done")[-1].replace('%','').replace(" ",'')
    StatusList=FetchedMcMStatus.replace("MCM:",'').split("%")
    StringDONEinMCM=''
    for j in StatusList:
        if 'done' in j: StringDONEinMCM=j.split("done")[-1].replace('%','').replace(" ",'')
    if len(StringDONEinMCM)>0: PercetageDONE=float(StringDONEinMCM)
    else: PercetageDONE=0.0
    #FetchedProdStauts='PROD: '+StringOfStatus(i.PrepIds) #Full string with status
    FetchedProdStauts='PROD: '+PercentageProd(i.PrepIds)
    if PercetageDONE>=90.0:
        FillingTable=FillingTable+TemplateBlockDONE.replace('REQUEST',i.Name).replace('CONTACT',i.Contact).replace('ANALYZER',i.Analyzer).replace('REQI',i.PrepIds[0]).replace('REQF',i.PrepIds[-1]).replace('STATUS',FetchedMcMStatus+' and '+FetchedProdStauts).replace('CAM',FetchedMcMCampaigns)
    elif PercetageDONE>=50.0 and PercetageDONE<90.0:
        FillingTable=FillingTable+TemplateBlockHALFDONE.replace('REQUEST',i.Name).replace('CONTACT',i.Contact).replace('ANALYZER',i.Analyzer).replace('REQI',i.PrepIds[0]).replace('REQF',i.PrepIds[-1]).replace('STATUS',FetchedMcMStatus+' and '+FetchedProdStauts).replace('CAM',FetchedMcMCampaigns)
    else:
        FillingTable=FillingTable+TemplateBlockSTUCK.replace('REQUEST',i.Name).replace('CONTACT',i.Contact).replace('ANALYZER',i.Analyzer).replace('REQI',i.PrepIds[0]).replace('REQF',i.PrepIds[-1]).replace('STATUS',FetchedMcMStatus+' and '+FetchedProdStauts).replace('CAM',FetchedMcMCampaigns)
    msg = 'From: jruizalv@cern.ch\nSubject: Status of your EXO MC requests\n\nDear EXO analyzer,\n\nYour MC EXO requests from '+i.PrepIds[0]+' to '+i.PrepIds[-1]+' are in status:\n'+FetchedMcMStatus+'\n\n'+FetchedProdStauts+'\n\nPlease check:\nhttp://jruizalv.web.cern.ch/jruizalv/'+SiteName+'/ \nfor more details. Moreover, if you do not see any status for your requests please take a look at the McM link.\n\nBest regards,\nMC&I group'
    #FinalEmails=i.Emails.append('cms-exo-mcrequests@cern.ch')
    FinalEmails=i.Emails
    MessagesToBeSent.append(msg)
    EmailAddresses.append(FinalEmails)
    if DEBUG:
        print FillingTable
    kcounter=kcounter+1

if DoNotify: 
    #Getting username and password to send email notifications
    LoginArgs=GetPassword.main(True)
    User=LoginArgs.username
    if User=='root': User = 'jruizalv'
    Password=LoginArgs.password.value
    #Setting STMP
    server = smtplib.SMTP('smtp.cern.ch', 587)
    server.starttls()
    server.login(User, Password)

for i in range(len(ListOfRequests)):
    if DoNotify and i.Notification: server.sendmail(User+"@cern.ch", EmailAddresses[i], MessagesToBeSent[i])
    if DEBUG:
        print "A notification email to", EmailAddresses[i], "has been sent"

#cmd.getoutput('sed -i -- "s#FILLTABLEHERE#'+FillingTable+'#g" '+BaseDirectory+SiteName+'/index.html')
index_html=open(BaseDirectory+SiteName+'/index.html','r')
html_lines=index_html.readlines()
index_html.close()
html_lines[html_lines.index('FILLTABLEHERE\n')]=FillingTable
index_html=open(BaseDirectory+SiteName+'/index.html','w')
index_html.writelines(html_lines)
index_html.close()

df.to_csv(StringITime.replace("-","").replace(" ","")+".csv")
