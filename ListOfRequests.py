#Structure of each dictionary entry is ----> (Request name, [Analyzer,[emails]], [Contact,email]): [List of prepids]
#DictionaryOfRequests={
#    ('MonoZ validation',['Andreas Albert',['jose.ruiz@cern.ch']],['Jose Ruiz','jose.ruiz@cern.ch']): ['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250']
#}
#
#def ListOfRequests(Initial,Final):
#    Base=Initial.split("-")[0]+"-"+Initial.split("-")[1]+"-"
#    Inum=int(Initial.split("-")[-1])
#    Fnum=int(Final.split("-")[-1])
#    FinalList=[]
#    for i in xrange(Inum,Fnum+1):
#        HowManyDigits=len(str(i))
#        ZerosString='00000'
#        FinalList.append(Base+ZerosString[:len(ZerosString)-HowManyDigits]+str(i))
#    return FinalList
#
#class EXORequest:
#    def __init__(self, RequestName, Analyzer, Contact, ListOfPrepids, ListOfEmails, Notify):
#        self.Name = RequestName
#        self.Analyzer = Analyzer
#        self.Contact = Contact
#        self.PrepIds = ListOfPrepids
#        self.Emails = ListOfEmails
#        self.Notification = Notify
#        self.Status = {}

from DataStructure import *

#List of requests (Name, Requestor, Contact, ListOfrequests, list of emails to notify)
MonoZ=EXORequest('MonoZ validation','Andreas Albert','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250'], ['andreas.albert@cern.ch'], False)
Req01=EXORequest('Displaced stop 2016','Juliette Alimena','Young Do',ListOfRequests('EXO-RunIISummer15GS-11311','EXO-RunIISummer15GS-11378'), [''], False)
Req02=EXORequest('Displaced stop 2017','Juliette Alimena','Young Do',ListOfRequests('EXO-RunIIFall17GS-01060','EXO-RunIIFall17GS-01127'), [''], False)
Req03=EXORequest('Displace sbottom 2016','Juliette Alimena','Young Do',ListOfRequests('EXO-RunIISummer15GS-11379','EXO-RunIISummer15GS-11402'), [''], False)
Req04=EXORequest('Q/B star 2017 part 1','Shalini Tukur','Bora',ListOfRequests('EXO-RunIIFall17GS-01000','EXO-RunIIFall17GS-01059'), [''], False)
Req05=EXORequest('E/Mu star 2017 part 2','Shalini Tukur','Bora',ListOfRequests('EXO-RunIIFall17GS-00942','EXO-RunIIFall17GS-00999'), [''], False)
Req06=EXORequest('Semi-Invisible Higgs 2016','','Bora',ListOfRequests('EXO-RunIIWinter15wmLHE-03125','EXO-RunIIWinter15wmLHE-03127'), [''], False)
Req07=EXORequest('BFF ZprimeToMuMu 2016','Minsuk Kim','Young Do',ListOfRequests('EXO-RunIISummer15wmLHEGS-06316','EXO-RunIISummer15wmLHEGS-06328'), ['sunil.dogra@cern.ch'], False)
Req08=EXORequest('BFF ZprimeToMuMu 2017','Minsuk Kim','Young Do',ListOfRequests('EXO-RunIIFall17wmLHEGS-00337','EXO-RunIIFall17wmLHEGS-00349'), ['sunil.dogra@cern.ch'], False)
Req09=EXORequest('GMSB 2017','Kevin','Shubhanshu',ListOfRequests('EXO-RunIIFall17GS-01140','EXO-RunIIFall17GS-01173'), ['kpm82@cornell.edu'], False)
Req10=EXORequest('Dilepton SM TT and WW 2017','','Young Do',ListOfRequests('EXO-RunIIFall17pLHE-00168','EXO-RunIIFall17pLHE-00179'), [''], False)
Req11=EXORequest('WGamma Resonance 1','Josh Kunkle','Young Do',ListOfRequests('EXO-RunIIFall17GS-01222','EXO-RunIIFall17GS-01269'), ['jkunkle@cern.ch'], True)
Req12=EXORequest('WGamma Resonance 2','Josh Kunkle','Young Do',ListOfRequests('EXO-RunIIFall17wmLHEGS-00398','EXO-RunIIFall17wmLHEGS-00445'), ['jkunkle@cern.ch'], True)
Req13=EXORequest('WGamma Resonance 3','Josh Kunkle','Young Do',ListOfRequests('EXO-RunIIFall17GS-01174','EXO-RunIIFall17GS-01221'), ['jkunkle@cern.ch'], True)
Req14=EXORequest('WGamma Resonance 4','Josh Kunkle','Young Do',ListOfRequests('EXO-RunIIFall17wmLHEGS-00350','EXO-RunIIFall17wmLHEGS-00397'), ['jkunkle@cern.ch'], True)
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
#print FirstPart
Req15=EXORequest('Heavy Neutrino 1','Sihyun Jeon','Shubhanshu',FirstPart, ['si.hyun.jeon@cern.ch'], True)
########################################################################################################
Req16=EXORequest('Heavy Neurtino 2','Sihyun Jeon','Shubhanshu',['EXO-RunIISummer15wmLHEGS-05531','EXO-RunIISummer15wmLHEGS-05532','EXO-RunIISummer15wmLHEGS-05533','EXO-RunIISummer15wmLHEGS-05534','EXO-RunIISummer15wmLHEGS-05535','EXO-RunIISummer15wmLHEGS-05536','EXO-RunIISummer15wmLHEGS-05538','EXO-RunIISummer15wmLHEGS-05539','EXO-RunIISummer15wmLHEGS-05540','EXO-RunIISummer15wmLHEGS-05541','EXO-RunIISummer15wmLHEGS-05542','EXO-RunIISummer15wmLHEGS-05544','EXO-RunIISummer15wmLHEGS-05545','EXO-RunIISummer15wmLHEGS-05546','EXO-RunIISummer15wmLHEGS-05547','EXO-RunIISummer15wmLHEGS-05548','EXO-RunIISummer15wmLHEGS-05550','EXO-RunIISummer15wmLHEGS-05551','EXO-RunIISummer15wmLHEGS-05552','EXO-RunIISummer15wmLHEGS-05553','EXO-RunIISummer15wmLHEGS-05554','EXO-RunIISummer15wmLHEGS-05555','EXO-RunIISummer15wmLHEGS-05556','EXO-RunIISummer15wmLHEGS-05557','EXO-RunIISummer15wmLHEGS-05558','EXO-RunIISummer15wmLHEGS-05559','EXO-RunIISummer15wmLHEGS-05560','EXO-RunIISummer15wmLHEGS-05561','EXO-RunIISummer15wmLHEGS-05562','EXO-RunIISummer15wmLHEGS-05563','EXO-RunIISummer15wmLHEGS-05564','EXO-RunIISummer15wmLHEGS-05565'], ['si.hyun.jeon@cern.ch'], True)
Req17=EXORequest('Heavy Neurtino 3','Sihyun Jeon','Shubhanshu',['EXO-RunIISummer15wmLHEGS-05566','EXO-RunIISummer15wmLHEGS-05567','EXO-RunIISummer15wmLHEGS-05568','EXO-RunIISummer15wmLHEGS-05570','EXO-RunIISummer15wmLHEGS-05571','EXO-RunIISummer15wmLHEGS-05572','EXO-RunIISummer15wmLHEGS-05573','EXO-RunIISummer15wmLHEGS-05574','EXO-RunIISummer15wmLHEGS-05575','EXO-RunIISummer15wmLHEGS-05576','EXO-RunIISummer15wmLHEGS-05577','EXO-RunIISummer15wmLHEGS-05578','EXO-RunIISummer15wmLHEGS-05579','EXO-RunIISummer15wmLHEGS-05580','EXO-RunIISummer15wmLHEGS-05581','EXO-RunIISummer15wmLHEGS-05582','EXO-RunIISummer15wmLHEGS-05583','EXO-RunIISummer15wmLHEGS-05584','EXO-RunIISummer15wmLHEGS-05585','EXO-RunIISummer15wmLHEGS-05586','EXO-RunIISummer15wmLHEGS-05587','EXO-RunIISummer15wmLHEGS-05588','EXO-RunIISummer15wmLHEGS-05589','EXO-RunIISummer15wmLHEGS-05590','EXO-RunIISummer15wmLHEGS-05591','EXO-RunIISummer15wmLHEGS-05592','EXO-RunIISummer15wmLHEGS-05593','EXO-RunIISummer15wmLHEGS-05594','EXO-RunIISummer15wmLHEGS-05595','EXO-RunIISummer15wmLHEGS-05596','EXO-RunIISummer15wmLHEGS-05597'], ['si.hyun.jeon@cern.ch'], True)
Req18=EXORequest('Heavy Neurtino 4','Sihyun Jeon','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05598','EXO-RunIISummer15wmLHEGS-05642'), ['si.hyun.jeon@cern.ch'], True)
Req19=EXORequest('Heavy Neurtino 5','Sihyun Jeon','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05644','EXO-RunIISummer15wmLHEGS-05676'), ['si.hyun.jeon@cern.ch'], True)
Req20=EXORequest('Heavy Neurtino 6','Sihyun Jeon','Shubhanshu',['EXO-RunIISummer15wmLHEGS-05678','EXO-RunIISummer15wmLHEGS-05679','EXO-RunIISummer15wmLHEGS-05680','EXO-RunIISummer15wmLHEGS-05681','EXO-RunIISummer15wmLHEGS-05682','EXO-RunIISummer15wmLHEGS-05683','EXO-RunIISummer15wmLHEGS-05684','EXO-RunIISummer15wmLHEGS-05685','EXO-RunIISummer15wmLHEGS-05686','EXO-RunIISummer15wmLHEGS-05687','EXO-RunIISummer15wmLHEGS-05688','EXO-RunIISummer15wmLHEGS-05690','EXO-RunIISummer15wmLHEGS-05691','EXO-RunIISummer15wmLHEGS-05692','EXO-RunIISummer15wmLHEGS-05693','EXO-RunIISummer15wmLHEGS-05694','EXO-RunIISummer15wmLHEGS-05695','EXO-RunIISummer15wmLHEGS-05696','EXO-RunIISummer15wmLHEGS-05697','EXO-RunIISummer15wmLHEGS-05698','EXO-RunIISummer15wmLHEGS-05699','EXO-RunIISummer15wmLHEGS-05700'], ['si.hyun.jeon@cern.ch'], True)
Req21=EXORequest('Heavy Neurtino 7','Sihyun Jeon','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05700','EXO-RunIISummer15wmLHEGS-05733'), ['si.hyun.jeon@cern.ch'], True)
Req22=EXORequest('Heavy Neurtino 8','Sihyun Jeon','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-05736','EXO-RunIISummer15wmLHEGS-05780'), ['si.hyun.jeon@cern.ch'], True)
Req23=EXORequest('VLL','Shubhanshu','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-06329','EXO-RunIISummer15wmLHEGS-06347'), [''], False)
Req24=EXORequest('LUX QED Gamma Gamma To LL','Laurent Thomas','Camilo',ListOfRequests('EXO-RunIIFall17GS-01270','EXO-RunIIFall17GS-01285'), ['uzzie.perez@cern.ch'], True)
Req25=EXORequest('RSGraviton To GammaGamma 1','Uzziel Perez','Camilo',ListOfRequests('EXO-RunIIFall17GS-01787','EXO-RunIIFall17GS-01815'), ['uzzie.perez@cern.ch'], True)
Req26=EXORequest('RSGraviton To GammaGamma 2','Uzziel Perez','Camilo',ListOfRequests('EXO-RunIIFall17GS-01816','EXO-RunIIFall17GS-01843'), ['uzzie.perez@cern.ch'], True)
Req27=EXORequest('ADD Graviton to GammaGamma 1','Uzziel Perez','Camilo',ListOfRequests('EXO-RunIIFall17GS-01844','EXO-RunIIFall17GS-01880'), ['uzzie.perez@cern.ch'], True)
Req28=EXORequest('ADD Graviton to GammaGamma 2','Uzziel Perez','Camilo',ListOfRequests('EXO-RunIIFall17GS-01881','EXO-RunIIFall17GS-01917'), ['uzzie.perez@cern.ch'], True)
Req29=EXORequest('ADD Graviton to GammaGamma 3','Uzziel Perez','Camilo',ListOfRequests('EXO-RunIIFall17GS-01918','EXO-RunIIFall17GS-01951'), ['uzzie.perez@cern.ch'], True)
#Req30=EXORequest('Semi-Invisible Higgs','','Bora',ListOfRequests('EXO-RunIIWinter15wmLHE-03125','EXO-RunIIWinter15wmLHE-03127'), [''], True)
Req31=EXORequest('Dark Photon 2016','Swagata Mukherjee','Jose',ListOfRequests('EXO-RunIISummer15wmLHEGS-06348','EXO-RunIISummer15wmLHEGS-06375'), ['physics.swagata@gmail.com'], True)
Req32=EXORequest('Dark Photon 2017','Swagata Mukherjee','Jose',ListOfRequests('EXO-RunIIFall17wmLHEGS-00476','EXO-RunIIFall17wmLHEGS-00503'), ['physics.swagata@gmail.com'], True)
Req33=EXORequest('Dark Photon 2018','Swagata Mukherjee','Jose',ListOfRequests('EXO-RunIIFall18wmLHEGS-00011','EXO-RunIIFall18wmLHEGS-00038'), ['physics.swagata@gmail.com'], True)
Req34=EXORequest('DMSimp MonoZ 2017','Andreas Albert','Jose',ListOfRequests('EXO-RunIIFall17wmLHEGS-00549','EXO-RunIIFall17wmLHEGS-00616'), ['andreas.albert@cern.ch'], True)
Req35=EXORequest('DMSimp MonoZ 2018','Andreas Albert','Jose',ListOfRequests('EXO-RunIIFall18wmLHEGS-00039','EXO-RunIIFall18wmLHEGS-00106'), ['andreas.albert@cern.ch'], True)
Req36=EXORequest('Delayed jets 2016','Matthew Citron','David',ListOfRequests('EXO-RunIISummer15GS-13704','EXO-RunIISummer15GS-13787'), ['matthew.citron@cern.ch'], True)
Req37=EXORequest('Delayed jets 2017','Matthew Citron','David',ListOfRequests('EXO-RunIIFall17GS-01512','EXO-RunIIFall17GS-01595'), ['matthew.citron@cern.ch'], True)
Req38=EXORequest('Delayed jets 2018','Matthew Citron','David',ListOfRequests('EXO-RunIIFall18GS-00181','EXO-RunIIFall18GS-00264'), ['matthew.citron@cern.ch'], True)
Req39=EXORequest('RPV neutralino 2016','Matthew Citron','David',ListOfRequests('EXO-RunIISummer15GS-13789','EXO-RunIISummer15GS-13824'), ['matthew.citron@cern.ch'], True)
Req40=EXORequest('RPV neutralino 2017','Matthew Citron','David',ListOfRequests('EXO-RunIIFall17GS-01596','EXO-RunIIFall17GS-01631'), ['matthew.citron@cern.ch'], True)
Req41=EXORequest('RPV neutralino 2018','Matthew Citron','David',ListOfRequests('EXO-RunIIFall18GS-00265','EXO-RunIIFall18GS-00300'), ['matthew.citron@cern.ch'], True)
Req42=EXORequest('Heavy Higgs to Diphoton','','Camilo',ListOfRequests('EXO-RunIIFall17GS-01634','EXO-RunIIFall17GS-01677'), [''], True)
Req43=EXORequest('Unpart Z To EE And MuMu 2017','Andreas Albert','Camilo',ListOfRequests('EXO-RunIIFall17GS-02412','EXO-RunIIFall17GS-02427'), ['andreas.albert@cern.ch'], True)
Req44=EXORequest('Unpart Z To EE And MuMu 2018','Andreas Albert','Camilo',ListOfRequests('EXO-RunIIFall18GS-00322','EXO-RunIIFall18GS-00337'), ['andreas.albert@cern.ch'], True)
Req45=EXORequest('Displaced Vertices 2017','Jordan Tucker','Bora',ListOfRequests('EXO-RunIIFall17GS-02237','EXO-RunIIFall17GS-02326'), ['[jordantucker@gmail.com'], True)
Req46=EXORequest('GluGlu to ZH 2017','Kyungwook Nam','Camilo',ListOfRequests('EXO-RunIIFall17GS-01634','EXO-RunIIFall17GS-01677'), ['kyungwook.nam@cern.ch'], True)
Req47=EXORequest('tt+scalar 2016','Maxi Heindl','David',ListOfRequests('EXO-RunIISummer15wmLHEGS-06421','EXO-RunIISummer15wmLHEGS-06546'), ['maximilian.heindl@cern.ch'], True)
Req48=EXORequest('tt+scalar 2017','Maxi Heindl','David',ListOfRequests('EXO-RunIIFall17wmLHEGS-00990','EXO-RunIIFall17wmLHEGS-01115'), ['maximilian.heindl@cern.ch'], True)
Req49=EXORequest('tt+scalar 2018','Maxi Heindl','David',ListOfRequests('EXO-RunIIFall18wmLHEGS-00357','EXO-RunIIFall18wmLHEGS-00482'), ['maximilian.heindl@cern.ch'], True)
Req50=EXORequest('Seesaw 2016','Maxi Heindl','David',ListOfRequests('EXO-RunIISummer15wmLHEGS-06547','EXO-RunIISummer15wmLHEGS-06606'), ['maximilian.heindl@cern.ch'], True)
Req51=EXORequest('Seesaw 2017','Maxi Heindl','David',ListOfRequests('EXO-RunIIFall17wmLHEGS-00930','EXO-RunIIFall17wmLHEGS-00989'), ['maximilian.heindl@cern.ch'], True)
Req52=EXORequest('Seesaw 2018','Maxi Heindl','David',ListOfRequests('EXO-RunIIFall18wmLHEGS-00297','EXO-RunIIFall18wmLHEGS-00356'), ['maximilian.heindl@cern.ch'], True)
Req53=EXORequest('Drell-Yan pT-binned','General','Jose',ListOfRequests('EXO-RunIIFall18wmLHEGS-00483','EXO-RunIIFall18wmLHEGS-00490'), [''], True)
Req54=EXORequest('PSeudoscalar2HDM MonoZLL 2016','Andreas Albert','Shubhanshu',ListOfRequests('EXO-RunIISummer15wmLHEGS-06376','EXO-RunIISummer15wmLHEGS-06420'), ['andreas.albert@cern.ch'], True)
Req55=EXORequest('PSeudoscalar2HDM MonoZLL 2017','Andreas Albert','Shubhanshu',ListOfRequests('EXO-RunIIFall17wmLHEGS-00504','EXO-RunIIFall17wmLHEGS-00548'), ['andreas.albert@cern.ch'], True)
Req56=EXORequest('PSeudoscalar2HDM MonoZLL 2018','Andreas Albert','Shubhanshu',ListOfRequests('EXO-RunIIFall18wmLHEGS-00107','EXO-RunIIFall18wmLHEGS-00151'), ['andreas.albert@cern.ch'], True)
Req57=EXORequest('MonoZ ADD 2017','Andreas Albert','Jane',ListOfRequests('EXO-RunIIFall17GS-02428','EXO-RunIIFall17GS-02448'), ['andreas.albert@cern.ch'], True)
Req58=EXORequest('MonoZ ADD 2018','Andreas Albert','Jane',ListOfRequests('EXO-RunIIFall18GS-00374','EXO-RunIIFall18GS-00394'), ['andreas.albert@cern.ch'], True)
Req59=EXORequest('FCP 2016','David Vannerom','Camilo',ListOfRequests('EXO-RunIISummer15GS-13826','EXO-RunIISummer15GS-13831'), ['david.vannerom@cern.ch'], True)
Req60=EXORequest('FCP 2017','David Vannerom','Camilo',ListOfRequests('EXO-RunIIFall17GS-02450','EXO-RunIIFall17GS-02455'), ['david.vannerom@cern.ch'], True)
Req61=EXORequest('FCP 2018','David Vannerom','Camilo',ListOfRequests('EXO-RunIIFall18GS-00653','EXO-RunIIFall18GS-00658'), ['david.vannerom@cern.ch'], True)
#Req6=EXORequest('','','',ListOfRequests('',''), [''], False)


#################################################################################

ListOfRequests=[]
#ListOfRequests.append(MonoZ)
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
ListOfRequests.append(Req23)
ListOfRequests.append(Req24)
ListOfRequests.append(Req25)
ListOfRequests.append(Req26)
ListOfRequests.append(Req27)
ListOfRequests.append(Req28)
ListOfRequests.append(Req29)
#ListOfRequests.append(Req30)
ListOfRequests.append(Req31)
ListOfRequests.append(Req32)
ListOfRequests.append(Req33)
ListOfRequests.append(Req34)
ListOfRequests.append(Req35)
ListOfRequests.append(Req36)
ListOfRequests.append(Req37)
ListOfRequests.append(Req38)
ListOfRequests.append(Req39)
ListOfRequests.append(Req40)
ListOfRequests.append(Req41)
ListOfRequests.append(Req42)
ListOfRequests.append(Req43)
ListOfRequests.append(Req44)
ListOfRequests.append(Req45)
ListOfRequests.append(Req46)
ListOfRequests.append(Req47)
ListOfRequests.append(Req48)
ListOfRequests.append(Req49)
ListOfRequests.append(Req50)
ListOfRequests.append(Req51)
ListOfRequests.append(Req52)
ListOfRequests.append(Req53)
ListOfRequests.append(Req54)
ListOfRequests.append(Req55)
ListOfRequests.append(Req56)
ListOfRequests.append(Req57)
ListOfRequests.append(Req58)
ListOfRequests.append(Req59)
ListOfRequests.append(Req60)
ListOfRequests.append(Req61)
#ListOfRequests.append(Req)
