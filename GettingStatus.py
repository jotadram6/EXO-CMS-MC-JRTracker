import urllib
import urllib2

def StringOfStatus(ListOfReq):
    FullStatus=''
    urlReqBase = 'https://dmytro.web.cern.ch/dmytro/cmsprodmon/workflows.php?prep_id=task_'
    for i in ListOfReq:
        req = urllib2.Request(urlReqBase+i)
        response = urllib2.urlopen(req)
        ListOfLines=response.readlines()
        for j in ListOfLines:
            if "Production status" in j: 
                CurrentStatus=j.replace('>','').replace('<','').replace('/','').replace('td','').replace('tr','').replace('lpc','').replace('\n','').split('=')[-1]
                FullStatus=FullStatus+CurrentStatus+' '
    return FullStatus

def PercentageProd(ListOfReq):
    StringToStrip=StringOfStatus(ListOfReq)
    if len(StringToStrip)<=1: return ""
    FullListStatus=StringToStrip.split(" ")
    FullListStatus=list(filter(lambda a: a != '', FullListStatus))
    NotRepeatedStatus=list(set(FullListStatus))
    PercentageStatus=""
    for i in xrange(len(NotRepeatedStatus)):
        PercentageStatus=PercentageStatus+NotRepeatedStatus[i]+" %.1f %% " % (100*len([j for j in FullListStatus if j==NotRepeatedStatus[i]])/len(FullListStatus))
    return PercentageStatus

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import *

def McMStatus(ListOfReq):
    FullStatus=''
    mcm = restful(dev=True)
    for i in ListOfReq:
        ReqDictionary=mcm.getA('requests', i, method='get')
        if len(ReqDictionary)==0: continue
        FullStatus=FullStatus+ReqDictionary['status']+' '
    return FullStatus
    
