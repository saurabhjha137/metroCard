class centralSummary :

    def __init__(self, collectionAmount = 0, discount = 0) :
        self.collectionAmount = collectionAmount
        self.discount = discount 
        self.adultCount = 0
        self.seniorCitizenCount = 0
        self.kidCount = 0

    def addToCollection(self, passengerFare) :
        self.collectionAmount += passengerFare

    def addToDiscount(self, discountAmount) :
        self.discount += discountAmount
    
    def updateKidCount(self) :
        self.kidCount += 1
    def updateAdultCount(self) :
        self.adultCount += 1
    def updateSeniorCitizenCount(self) :
        self.seniorCitizenCount +=1

        
    def centralSummaryPrint (self) :
        print('TOTAL_COLLECTION CENTRAL ' + str(self.collectionAmount) + ' ' + str(self.discount))
        if self.adultCount > 0 :
            print('ADULT ' + str(self.adultCount))
        if self.kidCount > 0 :
            print('KID ' + str(self.kidCount))
        if self.seniorCitizenCount > 0 :
            print('SENIOR_CITIZEN ' + str(self.seniorCitizenCount))
        