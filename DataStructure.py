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
        self.Status = {}

