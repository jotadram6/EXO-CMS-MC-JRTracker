#Structure of each dictionary entry is ----> (Request name, [Analyzer,[emails]], [Contact,email]): [List of prepids]
#DictionaryOfRequests={
#    ('MonoZ validation',['Andreas Albert',['jose.ruiz@cern.ch']],['Jose Ruiz','jose.ruiz@cern.ch']): ['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250']
#}

def ListOfRequests(Initial,Final):
    Base=Initial.split("-")[0]+"-"+Initial.split("-")[1]+"-"
    Inum=int(Initial.split("-")[-1])
    Fnum=int(Final.split("-")[-1])
    FinalList=[]
    for i in xrange(Inum,Fnum+1):
        HowManyDigits=len(str(i))
        ZerosString='00000'
        FinalList.append(Base+ZerosString[:len(ZerosString)-HowManyDigits]+str(i))
    return FinalList

class EXORequest:
    def __init__(self, RequestName, Analyzer, Contact, ListOfPrepids, ListOfEmails, Notify):
        self.Name = RequestName
        self.Analyzer = Analyzer
        self.Contact = Contact
        self.PrepIds = ListOfPrepids
        self.Emails = ListOfEmails
        self.Notification = Notify

#List of requests (Name, Requestor, Contact, ListOfrequests, list of emails to notify)
#MonoZ=EXORequest('MonoZ validation','Andreas Albert','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250'], ['andreas.albert@cern.ch'], False)
Req01=EXORequest('Displaced stop 2016','Juliette','Young Do',ListOfRequests('EXO-RunIISummer15GS-11311','EXO-RunIISummer15GS-11378'), [''], False)
Req02=EXORequest('Displaced stop 2017','Juliette','Young Do',ListOfRequests('EXO-RunIIFall17GS-01060','EXO-RunIIFall17GS-01127'), [''], False)
Req03=EXORequest('Displace sbottom 2016','Juliette Young Do','',ListOfRequests('EXO-RunIISummer15GS-11379','EXO-RunIISummer15GS-11402'), [''], False)
Req04=EXORequest('Q/B star 2017 part 1','','Bora',ListOfRequests('EXO-RunIIFall17GS-01000','EXO-RunIIFall17GS-01059'), [''], False)
Req05=EXORequest('Q/B star 2017 part 2','','Bora',ListOfRequests('EXO-RunIIFall17GS-00942','EXO-RunIIFall17GS-00999'), [''], False)
Req06=EXORequest('Semi-Invisible Higgs 2016','','Bora',ListOfRequests('EXO-RunIIWinter15wmLHE-03125','EXO-RunIIWinter15wmLHE-03127'), [''], False)
Req07=EXORequest('BFF ZprimeToMuMu 2016','Minsuk Kim','Young Do',ListOfRequests('EXO-RunIISummer15wmLHEGS-06316','EXO-RunIISummer15wmLHEGS-06328'), [''], False)
Req08=EXORequest('BFF ZprimeToMuMu 2017','Minsuk Kim','Young Do',ListOfRequests('EXO-RunIIFall17wmLHEGS-00337','EXO-RunIIFall17wmLHEGS-00349'), [''], False)
Req09=EXORequest('GMSB 2017','Kevin','Shubhanshu',ListOfRequests('EXO-RunIIFall17GS-01140','EXO-RunIIFall17GS-01173'), [''], False)
Req10=EXORequest('Dilepton SM TT and WW 2017','','Young Do',ListOfRequests('EXO-RunIIFall17pLHE-00168','EXO-RunIIFall17pLHE-00179'), [''], False)
Req11=EXORequest('WGamma Resonance 1','','Young Do',ListOfRequests('EXO-RunIIFall17GS-01222','EXO-RunIIFall17GS-01269'), [''], False)
Req12=EXORequest('WGamma Resonance 2','','Young Do',ListOfRequests('EXO-RunIIFall17wmLHEGS-00398','EXO-RunIIFall17wmLHEGS-00445'), [''], False)
Req13=EXORequest('WGamma Resonance 3','','Young Do',ListOfRequests('EXO-RunIIFall17GS-01174','EXO-RunIIFall17GS-01221'), [''], False)
Req14=EXORequest('WGamma Resonance 4','','Young Do',ListOfRequests('EXO-RunIIFall17wmLHEGS-00350','EXO-RunIIFall17wmLHEGS-00397'), [''], False)
#######################################################################################################
FirstPart=ListOfRequests('EXO-RunIISummer15wmLHEGS-05496','EXO-RunIISummer15wmLHEGS-05500')
#print FirstPart
SecondPart=ListOfRequests('EXO-RunIISummer15wmLHEGS-05505','EXO-RunIISummer15wmLHEGS-05522')
#print SecondPart
ThirdPart=ListOfRequests('EXO-RunIISummer15wmLHEGS-05524','EXO-RunIISummer15wmLHEGS-05530')
#print ThirdPart

FirstPart.append('EXO-RunIISummer15wmLHEGS-05502')
FirstPart.append('EXO-RunIISummer15wmLHEGS-05503')
FirstPart.extend(SecondPart)
FirstPart.extend(ThirdPart)
print FirstPart
Req15=EXORequest('Heavy Neutrino 1','Shiyun','Shubhanshu',FirstPart, [''], False)
########################################################################################################
Req16=EXORequest('Heavy Neurtino 2','Shiyun','Shubhanshu',['EXO-RunIISummer15wmLHEGS-05531','EXO-RunIISummer15wmLHEGS-05532','EXO-RunIISummer15wmLHEGS-05533','EXO-RunIISummer15wmLHEGS-05534','EXO-RunIISummer15wmLHEGS-05535','EXO-RunIISummer15wmLHEGS-05536','EXO-RunIISummer15wmLHEGS-05538','EXO-RunIISummer15wmLHEGS-05539','EXO-RunIISummer15wmLHEGS-05540','EXO-RunIISummer15wmLHEGS-05541','EXO-RunIISummer15wmLHEGS-05542','EXO-RunIISummer15wmLHEGS-05544','EXO-RunIISummer15wmLHEGS-05545','EXO-RunIISummer15wmLHEGS-05546','EXO-RunIISummer15wmLHEGS-05547','EXO-RunIISummer15wmLHEGS-05548','EXO-RunIISummer15wmLHEGS-05550','EXO-RunIISummer15wmLHEGS-05551','EXO-RunIISummer15wmLHEGS-05552','EXO-RunIISummer15wmLHEGS-05553','EXO-RunIISummer15wmLHEGS-05554','EXO-RunIISummer15wmLHEGS-05555','EXO-RunIISummer15wmLHEGS-05556','EXO-RunIISummer15wmLHEGS-05557','EXO-RunIISummer15wmLHEGS-05558','EXO-RunIISummer15wmLHEGS-05559','EXO-RunIISummer15wmLHEGS-05560','EXO-RunIISummer15wmLHEGS-05561','EXO-RunIISummer15wmLHEGS-05562','EXO-RunIISummer15wmLHEGS-05563','EXO-RunIISummer15wmLHEGS-05564','EXO-RunIISummer15wmLHEGS-05565'], [''], False)
Req17=EXORequest('Heavy Neurtino 3','Shiyun','Shubhanshu',['EXO-RunIISummer15wmLHEGS-05566','EXO-RunIISummer15wmLHEGS-05567','EXO-RunIISummer15wmLHEGS-05568','EXO-RunIISummer15wmLHEGS-05570','EXO-RunIISummer15wmLHEGS-05571','EXO-RunIISummer15wmLHEGS-05572','EXO-RunIISummer15wmLHEGS-05573','EXO-RunIISummer15wmLHEGS-05574','EXO-RunIISummer15wmLHEGS-05575','EXO-RunIISummer15wmLHEGS-05576','EXO-RunIISummer15wmLHEGS-05577','EXO-RunIISummer15wmLHEGS-05578','EXO-RunIISummer15wmLHEGS-05579','EXO-RunIISummer15wmLHEGS-05580','EXO-RunIISummer15wmLHEGS-05581','EXO-RunIISummer15wmLHEGS-05582','EXO-RunIISummer15wmLHEGS-05583','EXO-RunIISummer15wmLHEGS-05584','EXO-RunIISummer15wmLHEGS-05585','EXO-RunIISummer15wmLHEGS-05586','EXO-RunIISummer15wmLHEGS-05587','EXO-RunIISummer15wmLHEGS-05588','EXO-RunIISummer15wmLHEGS-05589','EXO-RunIISummer15wmLHEGS-05590','EXO-RunIISummer15wmLHEGS-05591','EXO-RunIISummer15wmLHEGS-05592','EXO-RunIISummer15wmLHEGS-05593','EXO-RunIISummer15wmLHEGS-05594','EXO-RunIISummer15wmLHEGS-05595','EXO-RunIISummer15wmLHEGS-05596','EXO-RunIISummer15wmLHEGS-05597'], [''], False)
Req18=EXORequest('Heavy Neurtino 4','Shiyun','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05598','EXO-RunIISummer15wmLHEGS-05642'), [''], False)
Req19=EXORequest('Heavy Neurtino 5','Shiyun','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05644','EXO-RunIISummer15wmLHEGS-05676'), [''], False)
Req20=EXORequest('Heavy Neurtino 6','Shiyun','Shubhanshu',['EXO-RunIISummer15wmLHEGS-05678','EXO-RunIISummer15wmLHEGS-05679','EXO-RunIISummer15wmLHEGS-05680','EXO-RunIISummer15wmLHEGS-05681','EXO-RunIISummer15wmLHEGS-05682','EXO-RunIISummer15wmLHEGS-05683','EXO-RunIISummer15wmLHEGS-05684','EXO-RunIISummer15wmLHEGS-05685','EXO-RunIISummer15wmLHEGS-05686','EXO-RunIISummer15wmLHEGS-05687','EXO-RunIISummer15wmLHEGS-05688','EXO-RunIISummer15wmLHEGS-05690','EXO-RunIISummer15wmLHEGS-05691','EXO-RunIISummer15wmLHEGS-05692','EXO-RunIISummer15wmLHEGS-05693','EXO-RunIISummer15wmLHEGS-05694','EXO-RunIISummer15wmLHEGS-05695','EXO-RunIISummer15wmLHEGS-05696','EXO-RunIISummer15wmLHEGS-05697','EXO-RunIISummer15wmLHEGS-05698','EXO-RunIISummer15wmLHEGS-05699','EXO-RunIISummer15wmLHEGS-05700'], [''], False)
Req21=EXORequest('Heavy Neurtino 7','Shiyun','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05700','EXO-RunIISummer15wmLHEGS-05733'), [''], False)
Req22=EXORequest('Heavy Neurtino 8','Shiyun','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05736','EXO-RunIISummer15wmLHEGS-05780'), [''], False)
#Req23=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req24=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req25=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req26=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req27=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req28=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req29=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req30=EXORequest('','','',ListOfRequests('',''), [''], False)
#Req7=EXORequest('','','',ListOfRequests('',''), [''], False)


#################################################################################

ListOfRequests=[]
ListOfRequests.append(MonoZ)
ListOfRequests.append(Req01)
ListOfRequests.append(Req02)
ListOfRequests.append(Req03)
ListOfRequests.append(Req04)
ListOfRequests.append(Req05)
ListOfRequests.append(Req06)
ListOfRequests.append(Req07)
ListOfRequests.append(Req08)
ListOfRequests.append(Req09)
ListOfRequests.append(Req10)
ListOfRequests.append(Req11)
ListOfRequests.append(Req12)
ListOfRequests.append(Req13)
ListOfRequests.append(Req14)
ListOfRequests.append(Req15)
ListOfRequests.append(Req16)
ListOfRequests.append(Req17)
ListOfRequests.append(Req18)
ListOfRequests.append(Req19)
ListOfRequests.append(Req20)
ListOfRequests.append(Req21)
ListOfRequests.append(Req22)
#ListOfRequests.append(Req)
