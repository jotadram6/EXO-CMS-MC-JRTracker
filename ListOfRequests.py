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

#List of requests
MonoZ=EXORequest('MonoZ validation','Andreas Albert','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250'], ['andreas.albert@cern.ch'], False)
DarkHiggs2016=EXORequest('Dark Higgs','Samuel Baxter','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05218',
                                                                   'EXO-RunIISummer15wmLHEGS-05219',
                                                                   'EXO-RunIISummer15wmLHEGS-05220',
                                                                   'EXO-RunIISummer15wmLHEGS-05221',
                                                                   'EXO-RunIISummer15wmLHEGS-05222',
                                                                   'EXO-RunIISummer15wmLHEGS-05223',
                                                                   'EXO-RunIISummer15wmLHEGS-05224',
                                                                   'EXO-RunIISummer15wmLHEGS-05225',
                                                                   'EXO-RunIISummer15wmLHEGS-05226',
                                                                   'EXO-RunIISummer15wmLHEGS-05227',
                                                                   'EXO-RunIISummer15wmLHEGS-05228',
                                                                   'EXO-RunIISummer15wmLHEGS-05229',
                                                                   'EXO-RunIISummer15wmLHEGS-05230',
                                                                   'EXO-RunIISummer15wmLHEGS-05231',
                                                                   'EXO-RunIISummer15wmLHEGS-05232',
                                                                   'EXO-RunIISummer15wmLHEGS-05233',
                                                                   'EXO-RunIISummer15wmLHEGS-05234',
                                                                   'EXO-RunIISummer15wmLHEGS-05235',
                                                                   'EXO-RunIISummer15wmLHEGS-05236',
                                                                   'EXO-RunIISummer15wmLHEGS-05237',
                                                                   'EXO-RunIISummer15wmLHEGS-05238',
                                                                   'EXO-RunIISummer15wmLHEGS-05239',
                                                                   'EXO-RunIISummer15wmLHEGS-05240',
                                                                   'EXO-RunIISummer15wmLHEGS-05241',
                                                                   'EXO-RunIISummer15wmLHEGS-05242',
                                                                   'EXO-RunIISummer15wmLHEGS-05243',
                                                                   'EXO-RunIISummer15wmLHEGS-05244',
                                                                   'EXO-RunIISummer15wmLHEGS-05245',
                                                                   'EXO-RunIISummer15wmLHEGS-05246',
                                                                   'EXO-RunIISummer15wmLHEGS-05247',
                                                                   'EXO-RunIISummer15wmLHEGS-05248'], ['samuel.baxter@desy.de'], False)
DiJet=EXORequest('DiJet','Cristina Mantilla','Jose Ruiz',['EXO-RunIIFall17wmLHEGS-00049',
                                                          'EXO-RunIIFall17wmLHEGS-00050',
                                                          'EXO-RunIIFall17wmLHEGS-00051',
                                                          'EXO-RunIIFall17wmLHEGS-00052',
                                                          'EXO-RunIIFall17wmLHEGS-00053',
                                                          'EXO-RunIIFall17wmLHEGS-00054',
                                                          'EXO-RunIIFall17wmLHEGS-00055',
                                                          'EXO-RunIIFall17wmLHEGS-00056',
                                                          'EXO-RunIIFall17wmLHEGS-00057',
                                                          'EXO-RunIIFall17wmLHEGS-00058',
                                                          'EXO-RunIIFall17wmLHEGS-00059',
                                                          'EXO-RunIIFall17wmLHEGS-00060',
                                                          'EXO-RunIIFall17wmLHEGS-00061',
                                                          'EXO-RunIIFall17wmLHEGS-00062',
                                                          'EXO-RunIIFall17wmLHEGS-00063',
                                                          'EXO-RunIIFall17wmLHEGS-00064',
                                                          'EXO-RunIIFall17wmLHEGS-00065',
                                                          'EXO-RunIIFall17wmLHEGS-00066',
                                                          'EXO-RunIIFall17wmLHEGS-00067',
                                                          'EXO-RunIIFall17wmLHEGS-00068',
                                                          'EXO-RunIIFall17wmLHEGS-00069',
                                                          'EXO-RunIIFall17wmLHEGS-00070',
                                                          'EXO-RunIIFall17wmLHEGS-00071',
                                                          'EXO-RunIIFall17wmLHEGS-00072',
                                                          'EXO-RunIIFall17wmLHEGS-00073',
                                                          'EXO-RunIIFall17wmLHEGS-00074',
                                                          'EXO-RunIIFall17wmLHEGS-00075',
                                                          'EXO-RunIIFall17wmLHEGS-00076',
                                                          'EXO-RunIIFall17wmLHEGS-00077',
                                                          'EXO-RunIIFall17wmLHEGS-00078',
                                                          'EXO-RunIIFall17wmLHEGS-00079',
                                                          'EXO-RunIIFall17wmLHEGS-00080'], ['cristina.ana.mantilla.suarez@cern.ch'], False)

ADDMonophoton=EXORequest('Monophoton ADD extension','Bhawna Gomber','Jose Ruiz',['EXO-RunIISummer15GS-11077',
                                                                                 'EXO-RunIISummer15GS-11078',
                                                                                 'EXO-RunIISummer15GS-11079',
                                                                                 'EXO-RunIISummer15GS-11080',
                                                                                 'EXO-RunIISummer15GS-11081',
                                                                                 'EXO-RunIISummer15GS-11082',
                                                                                 'EXO-RunIISummer15GS-11083',
                                                                                 'EXO-RunIISummer15GS-11084',
                                                                                 'EXO-RunIISummer15GS-11085',
                                                                                 'EXO-RunIISummer15GS-11086',
                                                                                 'EXO-RunIISummer15GS-11087',
                                                                                 'EXO-RunIISummer15GS-11088',
                                                                                 'EXO-RunIISummer15GS-11089',
                                                                                 'EXO-RunIISummer15GS-11090',
                                                                                 'EXO-RunIISummer15GS-11091'], ['Bhawna.Gomber@cern.ch'], False)

ADDMonophotonDMSimp=EXORequest('Monophoton DMsimp','Yutaro Iiyama','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05868',
                                                                                'EXO-RunIISummer15wmLHEGS-05869',
                                                                                'EXO-RunIISummer15wmLHEGS-05870',
                                                                                'EXO-RunIISummer15wmLHEGS-05871',
                                                                                'EXO-RunIISummer15wmLHEGS-05872',
                                                                                'EXO-RunIISummer15wmLHEGS-05873',
                                                                                'EXO-RunIISummer15wmLHEGS-05874',
                                                                                'EXO-RunIISummer15wmLHEGS-05875',
                                                                                'EXO-RunIISummer15wmLHEGS-05876',
                                                                                'EXO-RunIISummer15wmLHEGS-05877',
                                                                                'EXO-RunIISummer15wmLHEGS-05878',
                                                                                'EXO-RunIISummer15wmLHEGS-05879',
                                                                                'EXO-RunIISummer15wmLHEGS-05880',
                                                                                'EXO-RunIISummer15wmLHEGS-05881',
                                                                                'EXO-RunIISummer15wmLHEGS-05882',
                                                                                'EXO-RunIISummer15wmLHEGS-05883',
                                                                                'EXO-RunIISummer15wmLHEGS-05884',
                                                                                'EXO-RunIISummer15wmLHEGS-05885',
                                                                                'EXO-RunIISummer15wmLHEGS-05886',
                                                                                'EXO-RunIISummer15wmLHEGS-05887',
                                                                                'EXO-RunIISummer15wmLHEGS-05888',
                                                                                'EXO-RunIISummer15wmLHEGS-05889',
                                                                                'EXO-RunIISummer15wmLHEGS-05890',
                                                                                'EXO-RunIISummer15wmLHEGS-05891',
                                                                                'EXO-RunIISummer15wmLHEGS-05892',
                                                                                'EXO-RunIISummer15wmLHEGS-05893',
                                                                                'EXO-RunIISummer15wmLHEGS-05894',
                                                                                'EXO-RunIISummer15wmLHEGS-05895',
                                                                                'EXO-RunIISummer15wmLHEGS-05896',
                                                                                'EXO-RunIISummer15wmLHEGS-05897',
                                                                                'EXO-RunIISummer15wmLHEGS-05898',
                                                                                'EXO-RunIISummer15wmLHEGS-05899',
                                                                                'EXO-RunIISummer15wmLHEGS-05900',
                                                                                'EXO-RunIISummer15wmLHEGS-05901',
                                                                                'EXO-RunIISummer15wmLHEGS-05902',
                                                                                'EXO-RunIISummer15wmLHEGS-05903',
                                                                                'EXO-RunIISummer15wmLHEGS-05904',
                                                                                'EXO-RunIISummer15wmLHEGS-05905',
                                                                                'EXO-RunIISummer15wmLHEGS-05906',
                                                                                'EXO-RunIISummer15wmLHEGS-05907',
                                                                                'EXO-RunIISummer15wmLHEGS-05908',
                                                                                'EXO-RunIISummer15wmLHEGS-05909',
                                                                                'EXO-RunIISummer15wmLHEGS-05910',
                                                                                'EXO-RunIISummer15wmLHEGS-05911',
                                                                                'EXO-RunIISummer15wmLHEGS-05912',
                                                                                'EXO-RunIISummer15wmLHEGS-05913',
                                                                                'EXO-RunIISummer15wmLHEGS-05914',
                                                                                'EXO-RunIISummer15wmLHEGS-05915'], ['Yutaro.Iiyama@cern.ch'], False)

GGSherpa=EXORequest('Sherpa GG','Andrew Buccilli','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00163','EXO-RunIIFall17GS-00169'), ['andrew.buccilli@cern.ch'], True)

GGJetsSherpa=EXORequest('Sherpa GG Jets','Andrew Buccilli','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00170','EXO-RunIIFall17GS-00177'), ['andrew.buccilli@cern.ch'], True)

DisplacedSUSY=EXORequest('Displaced SUSY','Juliette Alimena','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00041','EXO-RunIIFall17GS-00100'), ['juliette.alimena@cern.ch'], True)

HSCP1=EXORequest('HSCP 1','Juliette Alimena','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00426','EXO-RunIIFall17GS-00476'), ['juliette.alimena@cern.ch'], True)

HSCP2=EXORequest('HSCP 2','Juliette Alimena','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00477','EXO-RunIIFall17GS-00529'), ['juliette.alimena@cern.ch'], True)

Trijet1HP=EXORequest('Trijet 2017 High Priority 1','Francesco Santanastasio','Youngdo Oh',ListOfRequests('EXO-RunIIFall17GS-00037','EXO-RunIIFall17GS-00040'), ['Francesco.Santanastasio@cern.ch'], True)

Trijet2HP=EXORequest('Trijet 2017 High Priority 2','Francesco Santanastasio','Youngdo Oh',ListOfRequests('EXO-RunIIFall17wmLHEGS-00105','EXO-RunIIFall17wmLHEGS-00108'), ['Francesco.Santanastasio@cern.ch'], True)

Trijet1=EXORequest('Trijet 2017 1','Francesco Santanastasio','Youngdo Oh',ListOfRequests('EXO-RunIIFall17GS-00101','EXO-RunIIFall17GS-00162'), ['Francesco.Santanastasio@cern.ch'], True)

Trijet2=EXORequest('Trijet 2017 2','Francesco Santanastasio','Youngdo Oh',ListOfRequests('EXO-RunIIFall17wmLHEGS-00109','EXO-RunIIFall17wmLHEGS-00170'), ['Francesco.Santanastasio@cern.ch'], True)

Trijet3=EXORequest('Trijet 2016 1','Francesco Santanastasio','Youngdo Oh',ListOfRequests('EXO-RunIISummer15GS-11102','EXO-RunIISummer15GS-11167'), ['Francesco.Santanastasio@cern.ch'], True)

Trijet4=EXORequest('Trijet 2016 2','Francesco Santanastasio','Youngdo Oh',ListOfRequests('EXO-RunIISummer15wmLHEGS-05954','EXO-RunIISummer15wmLHEGS-06019'), ['Francesco.Santanastasio@cern.ch'], True)

CI1=EXORequest('Contact Interactions 1','Prakash Thapa','Youngdo Oh',ListOfRequests('EXO-RunIIFall17GS-00178','EXO-RunIIFall17GS-00260'), ['prakash.thapa@wayne.edu'], True)

CI2=EXORequest('Contact Interactions 2','Prakash Thapa','Youngdo Oh',ListOfRequests('EXO-RunIIFall17GS-00261','EXO-RunIIFall17GS-00343'), ['prakash.thapa@wayne.edu'], True)

CI3=EXORequest('Contact Interactions 3','Prakash Thapa','Youngdo Oh',ListOfRequests('EXO-RunIIFall17GS-00344','EXO-RunIIFall17GS-00425'), ['prakash.thapa@wayne.edu'], True)

MonoLQ=EXORequest('Mono LQ','Abdollah Mohammadi','Youngdo Oh',ListOfRequests('EXO-RunIIFall17wmLHEGS-00171','EXO-RunIIFall17wmLHEGS-00235'), ['Abdollah.Mohammadi@cern.ch'], True)

HVDS=EXORequest('HVDS', 'Kevin McDermott','Shubhanshu Chauhan',ListOfRequests('EXO-RunIISummer15GS-10956','EXO-RunIISummer15GS-11039'),['kpm82@cornell.edu'], True)

HNS=EXORequest('Heavy Neutrino S channel','Sihyun Jeon','Shubhanshu Chauhan',ListOfRequests('EXO-RunIISummer15wmLHEGS-05598','EXO-RunIISummer15wmLHEGS-05781'),['si.hyun.jeon@cern.ch'], True)

HNT=EXORequest('Heavy Neutrino T channel','Sihyun Jeon','Shubhanshu Chauhan',ListOfRequests('EXO-RunIISummer15wmLHEGS-05496','EXO-RunIISummer15wmLHEGS-05597'),['si.hyun.jeon@cern.ch'], True)

VLL=EXORequest('VectorLikeleptons','Shubhanshu Chauhan','Shubhanshu Chauhan',ListOfRequests('EXO-RunIIFall17wmLHEGS-00082','EXO-RunIIFall17wmLHEGS-00100'),['shubhanshu.chauhan@cern.ch'], True)

WTauNu=EXORequest('WtoTauNu','Central','Shubhanshu Chauhan',ListOfRequests('EXO-RunIIFall17GS-00016','EXO-RunIIFall17GS-00024'),['cms-exo-mcrequests@cern.ch'], False)

STDM=EXORequest('SingleTopDM','Juliette Alimena','Shubhanshu Chauhan',ListOfRequests('EXO-PhaseIITDRFall17wmLHEGS-00001','EXO-PhaseIITDRFall17wmLHEGS-00006'),['juliette.alimena@cern.ch'], True)

DarkSUSY=EXORequest('Dark SUSY','Henning Keller','Jose Ruiz',ListOfRequests('EXO-PhaseIISummer17pLHE-00005','EXO-PhaseIISummer17pLHE-00034'),['henning.keller@cern.ch','juliette.alimena@cern.ch'], True)

ZprimeToZto4mu=EXORequest('ZprimeToZto4mu','Muhammad Ahmad','Bora Isildak',ListOfRequests('EXO-RunIISummer15wmLHEGS-06020','EXO-RunIISummer15wmLHEGS-06038'), ['m.ahmad@cern.ch'], True)

ttbarDMJets=EXORequest('ttbarDMJets','Kelly Beernaert ','Bora Isildak',ListOfRequests('EXO-PhaseIISummer17wmLHEGENOnly-00001','EXO-PhaseIISummer17wmLHEGENOnly-00014'), ['ksbeerna@cern.ch'], True)

LQ3=EXORequest('LQ3-YR','Yuta Takahashi ','Jose Ruiz',ListOfRequests('EXO-PhaseIISummer17wmLHEGENOnly-00015','EXO-PhaseIISummer17wmLHEGENOnly-00029'), ['Yuta.Takahashi@cern.ch'], True)

EmergingJets=EXORequest('EmergingJets-ReAOD','Kak Wong ','Jose Ruiz',ListOfRequests('EXO-RunIISummer15GS-11227','EXO-RunIISummer15GS-11228'), ['kakw@terpmail.umd.edu'], True)

DarkHiggsV2=EXORequest('Dark Higgs v2','Samuel Baxter','Jose Ruiz',ListOfRequests('EXO-RunIISummer15wmLHEGS-06039','EXO-RunIISummer15wmLHEGS-06048'), ['samuel.baxter@desy.de'], True)

DisplacedSUSYYR=EXORequest('Displaced SUSY YR','Pablo Martinez ','Jose Ruiz',ListOfRequests('EXO-PhaseIISummer17GenOnly-00001','EXO-PhaseIISummer17GenOnly-00110'), ['Pablo.Martinez@cern.ch'], True)

#################################################################################

ListOfRequests=[]
ListOfRequests.append(MonoZ)
ListOfRequests.append(DarkHiggs2016)
ListOfRequests.append(DiJet)
ListOfRequests.append(ADDMonophoton)
ListOfRequests.append(ADDMonophotonDMSimp)
ListOfRequests.append(GGSherpa)
ListOfRequests.append(GGJetsSherpa)
ListOfRequests.append(DisplacedSUSY)
ListOfRequests.append(HSCP1)
ListOfRequests.append(HSCP2)
ListOfRequests.append(Trijet1HP)
ListOfRequests.append(Trijet2HP)
ListOfRequests.append(Trijet1)
ListOfRequests.append(Trijet2)
ListOfRequests.append(Trijet3)
ListOfRequests.append(Trijet4)
ListOfRequests.append(CI1)
ListOfRequests.append(CI2)
ListOfRequests.append(CI3)
ListOfRequests.append(MonoLQ)
ListOfRequests.append(HVDS)
ListOfRequests.append(HNS)
ListOfRequests.append(HNT)
ListOfRequests.append(VLL)
ListOfRequests.append(WTauNu)
ListOfRequests.append(STDM)
ListOfRequests.append(DarkSUSY)
ListOfRequests.append(ZprimeToZto4mu)
ListOfRequests.append(ttbarDMJets)
ListOfRequests.append(LQ3)
ListOfRequests.append(EmergingJets)
ListOfRequests.append(DarkHiggsV2)
ListOfRequests.append(DisplacedSUSYYR)
#ListOfRequests.append
