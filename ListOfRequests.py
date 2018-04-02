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
    def __init__(self, RequestName, Analyzer, Contact, ListOfPrepids, ListOfEmails):
        self.Name = RequestName
        self.Analyzer = Analyzer
        self.Contact = Contact
        self.PrepIds = ListOfPrepids
        self.Emails = ListOfEmails

#List of requests
MonoZ=EXORequest('MonoZ validation','Andreas Albert','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250'], ['andreas.albert@cern.ch','cms-exo-mcrequests@cern.ch'])
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
                                                                   'EXO-RunIISummer15wmLHEGS-05248'], ['samuel.baxter@desy.de','cms-exo-mcrequests@cern.ch'])
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
                                                          'EXO-RunIIFall17wmLHEGS-00080'], ['cristina.ana.mantilla.suarez@cern.ch','cms-exo-mcrequests@cern.ch'])

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
                                                                                 'EXO-RunIISummer15GS-11091'], ['Bhawna.Gomber@cern.ch','cms-exo-mcrequests@cern.ch'])

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
                                                                                'EXO-RunIISummer15wmLHEGS-05915'], ['Yutaro.Iiyama@cern.ch','cms-exo-mcrequests@cern.ch'])

GGSherpa=EXORequest('Sherpa GG','Andrew Buccilli','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00163','EXO-RunIIFall17GS-00169'), ['andrew.buccilli@cern.ch','cms-exo-mcrequests@cern.ch'])

GGJetsSherpa=EXORequest('Sherpa GG Jets','Andrew Buccilli','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00170','EXO-RunIIFall17GS-00177'), ['andrew.buccilli@cern.ch','cms-exo-mcrequests@cern.ch'])

DisplacedSUSY=EXORequest('Displaced SUSY','Juliette Alimena','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00041','EXO-RunIIFall17GS-00100'), ['juliette.alimena@cern.ch','cms-exo-mcrequests@cern.ch'])

HSCP1=EXORequest('HSCP 1','Juliette Alimena','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00426','EXO-RunIIFall17GS-00476'), ['juliette.alimena@cern.ch','cms-exo-mcrequests@cern.ch'])

HSCP2=EXORequest('HSCP 2','Juliette Alimena','Jose Ruiz',ListOfRequests('EXO-RunIIFall17GS-00477','EXO-RunIIFall17GS-00529'), ['juliette.alimena@cern.ch','cms-exo-mcrequests@cern.ch'])

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
#ListOfRequests.append()
