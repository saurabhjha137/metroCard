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
        self.ifReturnJourney = 0
        self.travelDestination = None
        
    def getPassengerID (self) :
        return self.passengerID
    def getTravelDestination (self) :
        return self.travelDestination
    
    
    def getPassengerBalance (self) :
        return self.passengerBalance
    def updatePassengerBalance(self, updatedBalance) :
        self.passengerBalance = updatedBalance


    def deductTravelCharges(self, travellingDestination, passengerType, centralCollectionSummary) :
        
        if self.getTravelDestination() != travellingDestination :
            print('proceed')
            balance = self.getPassengerBalance()
            ##checking passenger Type
            if passengerType == 'ADULT' :
                ## checking if passenger has required balance
                if  balance >= ADULT_FARE :
                    updatedBalance = balance - ADULT_FARE
                    self.updatePassengerBalance(updatedBalance)
                    centralCollectionSummary.addToCollection(ADULT_FARE)

                ##if passenger not having required balance
                ##calculating service charges
                else :
                    serviceFeeCharge = calcServiceCharge(balance, ADULT_FARE)
                    updatedBalance = 0
                    self.updatePassengerBalance(updatedBalance)
                    centralCollectionSummary.addToCollection(ADULT_FARE+serviceFeeCharge)

            elif passengerType == 'SENIOR_CITIZEN' :

                if  balance >= SENIOR_CITIZEN_FARE :
                    updatedBalance = balance - SENIOR_CITIZEN_FARE
                    self.updatePassengerBalance(updatedBalance)
                    centralCollectionSummary.addToCollection(SENIOR_CITIZEN_FARE)

                else :
                    serviceFeeCharge = calcServiceCharge(balance, SENIOR_CITIZEN_FARE)
                    updatedBalance = 0
                    self.updatePassengerBalance(updatedBalance)
                    centralCollectionSummary.addToCollection(SENIOR_CITIZEN_FARE+serviceFeeCharge)

            elif passengerType == 'KID' :

                if  balance >= KID_FARE :
                    updatedBalance = balance - KID_FARE
                    self.updatePassengerBalance(updatedBalance)
                    centralCollectionSummary.addToCollection(KID_FARE)

                else :
                    serviceFeeCharge = calcServiceCharge(balance, KID_FARE)
                    updatedBalance = 0
                    self.updatePassengerBalance(updatedBalance)
                    centralCollectionSummary.addToCollection(KID_FARE+serviceFeeCharge)


        else :
            print ('travel Source and Destination are same')

    def printDetails (self):
        print ('------------------------------')
        print (' ID : ' + self.passengerID)
        print (' Balance : ' + self.passengerBalance)
        print ('------------------------------')

