class metroCardMembers :
    def __init__(self, memberID, memberBalance, memberType):
        self.memberID = memberID
        self.memberBalance =  memberBalance
        self.memberType =  memberType
    
    def printDetails (self):
        print ('------------------------------')
        print (' ID : ' + self.memberID)
        print (' Type : ' + self.memberType)
        print (' Balance : ' + self.memberBalance)
        print ('------------------------------')

