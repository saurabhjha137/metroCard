## round trip Pending
ADULT_FARE = 200
SENIOR_CITIZEN_FARE = 100
KID_FARE = 50
SERVICE_FEE = 2

def calcServiceCharge (balance, fare) :
    serviceCharge = fare - balance
    serviceCharge = serviceCharge*SERVICE_FEE
    return int(serviceCharge/100)

class metroCardPassengers :
    def __init__(self, passengerID, passengerBalance):
        self.passengerID = passengerID
        self.passengerBalance =  passengerBalance
        self.isReturnJourney = False
        self.travelDestination = None
        
    def getPassengerID (self) :
        return self.passengerID
    

    def getTravelDestination (self) :
        return self.travelDestination
    def updateTravelDestination(self, destination) :
        self.travelDestination = destination


    def getIsReturnJourney(self) :
        return self.isReturnJourney
    def updateIsReturnJourney(self, updateReturnJourney) :
        self.isReturnJourney = updateReturnJourney


    def getPassengerBalance (self) :
        return self.passengerBalance
    def updatePassengerBalance(self, updatedBalance) :
        self.passengerBalance = updatedBalance


    def deductTravelCharges(self, travellingDestination, passengerType, collectionSummary) :
        
        if  self.getTravelDestination() != travellingDestination :
            balance = int(self.getPassengerBalance())
            returnJourneyCheck = self.getIsReturnJourney()
            
            #if passenger doing OneWay Journey
            if returnJourneyCheck == False :

                ##checking passenger Type
                if  passengerType == 'ADULT' :
                    ## checking if passenger has required balance
                    if  balance >= ADULT_FARE :
                        updatedBalance = balance - ADULT_FARE
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(ADULT_FARE)
                        self.updateIsReturnJourney(True)
                        collectionSummary.updateAdultCount()
                    ##if passenger not having required balance
                    ##calculating service charges
                    else :
                        serviceFeeCharge = calcServiceCharge(balance, ADULT_FARE)
                        updatedBalance = 0
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(ADULT_FARE+serviceFeeCharge)
                        self.updateIsReturnJourney(True)
                        collectionSummary.updateAdultCount()

                elif passengerType == 'SENIOR_CITIZEN' :

                    if  balance >= SENIOR_CITIZEN_FARE :
                        updatedBalance = balance - SENIOR_CITIZEN_FARE
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(SENIOR_CITIZEN_FARE)
                        self.updateIsReturnJourney(True)
                        collectionSummary.updateSeniorCitizenCount()

                    else :
                        serviceFeeCharge = calcServiceCharge(balance, SENIOR_CITIZEN_FARE)
                        updatedBalance = 0
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(SENIOR_CITIZEN_FARE+serviceFeeCharge)
                        self.updateIsReturnJourney(True)
                        collectionSummary.updateSeniorCitizenCount()

                elif passengerType == 'KID' :

                    if  balance >= KID_FARE :
                        updatedBalance = balance - KID_FARE
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(KID_FARE)
                        self.updateIsReturnJourney(True)
                        collectionSummary.updateKidCount()

                    else :
                        serviceFeeCharge = calcServiceCharge(balance, KID_FARE)
                        updatedBalance = 0
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(KID_FARE+serviceFeeCharge)
                        self.updateIsReturnJourney(True)
                        collectionSummary.updateKidCount()

            #if passenger doing Return Journey        
            else :

                ##checking passenger Type
                if  passengerType == 'ADULT' :
                    ## checking if passenger has required balance
                    if  balance >= int(ADULT_FARE/2) :
                        updatedBalance = balance - int(ADULT_FARE/2)
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(int(ADULT_FARE/2))
                        collectionSummary.addToDiscount(int(ADULT_FARE/2))
                        collectionSummary.updateAdultCount()
                        self.updateIsReturnJourney(False)
                    ##if passenger not having required balance
                    ##calculating service charges
                    else :
                        serviceFeeCharge = calcServiceCharge(balance, int(ADULT_FARE/2))
                        updatedBalance = 0
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(int(ADULT_FARE/2) + serviceFeeCharge)
                        collectionSummary.addToDiscount(int(ADULT_FARE/2))
                        collectionSummary.updateAdultCount()
                        self.updateIsReturnJourney(False)

                elif passengerType == 'SENIOR_CITIZEN' :

                    if  balance >= int(SENIOR_CITIZEN_FARE/2) :
                        updatedBalance = balance - int(SENIOR_CITIZEN_FARE/2)
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(int(SENIOR_CITIZEN_FARE/2))
                        collectionSummary.addToDiscount(int(SENIOR_CITIZEN_FARE/2))
                        collectionSummary.updateSeniorCitizenCount()
                        self.updateIsReturnJourney(False)

                    else :
                        serviceFeeCharge = calcServiceCharge(balance, int(SENIOR_CITIZEN_FARE/2))
                        updatedBalance = 0
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(int(SENIOR_CITIZEN_FARE/2) + serviceFeeCharge)
                        collectionSummary.addToDiscount(int(SENIOR_CITIZEN_FARE/2))
                        collectionSummary.updateSeniorCitizenCount()
                        self.updateIsReturnJourney(False)

                elif passengerType == 'KID' :

                    if  balance >= int(KID_FARE/2) :
                        updatedBalance = balance - int(KID_FARE/2)
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(int(KID_FARE/2))
                        collectionSummary.addToDiscount(int(KID_FARE/2))
                        collectionSummary.updateKidCount()
                        self.updateIsReturnJourney(False)

                    else :
                        serviceFeeCharge = calcServiceCharge(balance, int(KID_FARE/2))
                        updatedBalance = 0
                        self.updatePassengerBalance(updatedBalance)
                        collectionSummary.addToCollection(int(KID_FARE/2) + serviceFeeCharge)
                        collectionSummary.addToDiscount(int(KID_FARE/2))
                        collectionSummary.updateKidCount()
                        self.updateIsReturnJourney(False)

            self.updateTravelDestination(travellingDestination)

        else :
            print ('travel Source and Destination are same')

    def printDetails (self):
        print ('------------------------------')
        print (' ID : ' + self.passengerID)
        print (' Balance : ' + str(self.passengerBalance))
        print ('------------------------------')

