#Structure of each dictionary entry is ----> (Request name, [Analyzer,[emails]], [Contact,email]): [List of prepids]
#DictionaryOfRequests={
#    ('MonoZ validation',['Andreas Albert',['jose.ruiz@cern.ch']],['Jose Ruiz','jose.ruiz@cern.ch']): ['EXO-RunIISummer15wmLHEGS-05249','EXO-RunIISummer15wmLHEGS-05250']
#}

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

ADDMonophoton=EXORequest('Monophoton ADD extension','Bhawna Gomber','Jose Ruiz',['EXO-RunIIFall17GS-00037',
                                                                                 'EXO-RunIIFall17GS-00038',
                                                                                 'EXO-RunIIFall17GS-00039',
                                                                                 'EXO-RunIIFall17GS-00040',
                                                                                 'EXO-RunIIFall17GS-00041',
                                                                                 'EXO-RunIIFall17GS-00042',
                                                                                 'EXO-RunIIFall17GS-00043',
                                                                                 'EXO-RunIIFall17GS-00044',
                                                                                 'EXO-RunIIFall17GS-00045',
                                                                                 'EXO-RunIIFall17GS-00046',
                                                                                 'EXO-RunIIFall17GS-00047',
                                                                                 'EXO-RunIIFall17GS-00048',
                                                                                 'EXO-RunIIFall17GS-00049',
                                                                                 'EXO-RunIIFall17GS-00050',
                                                                                 'EXO-RunIIFall17GS-00051'], ['Bhawna.Gomber@cern.ch','cms-exo-mcrequests@cern.ch'])

ListOfRequests=[]
ListOfRequests.append(MonoZ)
ListOfRequests.append(DarkHiggs2016)
ListOfRequests.append(DiJet)
ListOfRequests.append(ADDMonophoton)
