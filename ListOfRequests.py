#Structure of each dictionary entry is ----> (Request name, [Analyzer,[emails]], [Contact,email]): [List of prepids]
#DictionaryOfRequests={
#    ('MonoZ validation',['Andreas Albert',['jose.ruiz@cern.ch']],['Jose Ruiz','jose.ruiz@cern.ch']): ['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250']
#}

class EXORequest:
    def __init__(self, RequestName, Analyzer, Contact, ListOfPrepids):
        self.Name = RequestName
        self.Analyzer = Analyzer
        self.Contact = Contact
        self.PrepIds = ListOfPrepids

#List of requests
MonoZ=EXORequest('MonoZ validation','Andreas Albert','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250'])
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
                                                                   'EXO-RunIISummer15wmLHEGS-05248'])
DiJet=EXORequest('DiJet','Cristina Mantilla','Jose Ruiz',['EXO-RunIISummer15wmLHEGS-05253',
                                                          'EXO-RunIISummer15wmLHEGS-05254',
                                                          'EXO-RunIISummer15wmLHEGS-05255',
                                                          'EXO-RunIISummer15wmLHEGS-05256',
                                                          'EXO-RunIISummer15wmLHEGS-05257',
                                                          'EXO-RunIISummer15wmLHEGS-05258',
                                                          'EXO-RunIISummer15wmLHEGS-05259',
                                                          'EXO-RunIISummer15wmLHEGS-05260',
                                                          'EXO-RunIISummer15wmLHEGS-05261',
                                                          'EXO-RunIISummer15wmLHEGS-05262',
                                                          'EXO-RunIISummer15wmLHEGS-05263',
                                                          'EXO-RunIISummer15wmLHEGS-05264',
                                                          'EXO-RunIISummer15wmLHEGS-05265',
                                                          'EXO-RunIISummer15wmLHEGS-05266',
                                                          'EXO-RunIISummer15wmLHEGS-05267',
                                                          'EXO-RunIISummer15wmLHEGS-05268',
                                                          'EXO-RunIISummer15wmLHEGS-05269',
                                                          'EXO-RunIISummer15wmLHEGS-05270',
                                                          'EXO-RunIISummer15wmLHEGS-05271',
                                                          'EXO-RunIISummer15wmLHEGS-05272',
                                                          'EXO-RunIISummer15wmLHEGS-05273',
                                                          'EXO-RunIISummer15wmLHEGS-05274',
                                                          'EXO-RunIISummer15wmLHEGS-05275',
                                                          'EXO-RunIISummer15wmLHEGS-05276',
                                                          'EXO-RunIISummer15wmLHEGS-05277',
                                                          'EXO-RunIISummer15wmLHEGS-05278',
                                                          'EXO-RunIISummer15wmLHEGS-05279',
                                                          'EXO-RunIISummer15wmLHEGS-05280',
                                                          'EXO-RunIISummer15wmLHEGS-05281',
                                                          'EXO-RunIISummer15wmLHEGS-05282',
                                                          'EXO-RunIISummer15wmLHEGS-05283'])

ListOfRequests=[]
ListOfRequests.append(MonoZ)
ListOfRequests.append(DarkHiggs2016)
ListOfRequests.append(DiJet)
