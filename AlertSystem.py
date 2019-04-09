def Alerting(PrepID,S,Sm1,Sm3,DeltaEvents):
    if S=="new" and Sm1=="new":
        return "Action from MC contact needed: "+PrepID+" is in status new."
    if S=="defined" and Sm1=="defined":
        return "Action from MC contact needed: "+PrepID+" has not been approved."
    if S=="approved" and (Sm1=="defined" or Sm1=="approved"):
        return "Action from MC contact needed: "+PrepID+" has not been submitted."
    if S=="submitted" and Sm3=="submitted" and DeltaEvents<100:
        return "Please check everything seems fine with: "+PrepID+", the number of events produced in the last three weeks has been nearly zero."

