## round trip Pending
ADULT_FARE = 200
SENIOR_CITIZEN_FARE = 100
KID_FARE = 50
SERVICE_FEE = 2
REDUCTION_VALUE = 0.5

def calcServiceCharge (balance, fare) :
    serviceCharge = fare - balance
    serviceCharge = serviceCharge*SERVICE_FEE
    return int(serviceCharge/100)

def reduceFare(fare) :
    return int(fare * REDUCTION_VALUE)

class metroCardPassengers :
    def __init__(self, passengerID, passengerBalance, ReturnJourney = False , travelDestination = None):
        self.passengerID = passengerID
        self.passengerBalance =  passengerBalance
        self.returnJourney = ReturnJourney
        self.travelDestination = travelDestination
        
    def getPassengerID (self) :
        return self.passengerID
    

    def getTravelDestination (self) :
        return self.travelDestination
    def updateTravelDestination(self, destination) :
        self.travelDestination = destination


    def isReturnJourney(self) :
        return self.returnJourney
    def updateIsReturnJourney(self, updatedReturnJourney) :
        self.returnJourney = updatedReturnJourney


    def getPassengerBalance (self) :
        return int(self.passengerBalance)
    def updatePassengerBalance(self, updatedBalance) :
        self.passengerBalance = int(updatedBalance)

    #Passenger Has Enough balance to travel, hence deducting Fare
    def deductPassengerBalance(self, fare, balance, collectionSummary) :
        updatedBalance = balance - fare
        self.updatePassengerBalance(updatedBalance)
        collectionSummary.addToCollection(fare)
        
        

    #Passenger does not have Enough balance to travel, hence deducting Fare and applying Service charges
    def deductServiceChargeAndPassengerBalance(self, fare, balance, collectionSummary) :
        serviceFeeCharge = calcServiceCharge(balance, fare)
        updatedBalance = 0
        self.updatePassengerBalance(updatedBalance)
        collectionSummary.addToCollection(fare+serviceFeeCharge)
        
        

    #checking if Passenger Having Enough balance to travel
    def checkBalanceAndDeduct(self, fare , collectionSummary) :
        if  self.getPassengerBalance() >= fare :
            self.deductPassengerBalance(fare, self.getPassengerBalance(), collectionSummary)
        else :
            self.deductServiceChargeAndPassengerBalance(fare, self.getPassengerBalance(),collectionSummary)

    #Passenger is Doing Return Journey, hence Reduced fare will be deducted
    def deductForReturnJourney(self, passengerType, collectionSummary):
        #checking PassengerType
        if passengerType == 'ADULT' :
            self.checkBalanceAndDeduct(reduceFare(ADULT_FARE), collectionSummary)
            collectionSummary.updateAdultCount()
            collectionSummary.addToDiscount(reduceFare(ADULT_FARE))
                        
        elif passengerType == 'SENIOR_CITIZEN' :
            self.checkBalanceAndDeduct(reduceFare(SENIOR_CITIZEN_FARE), collectionSummary)
            collectionSummary.updateSeniorCitizenCount()
            collectionSummary.addToDiscount(reduceFare(SENIOR_CITIZEN_FARE))

        elif passengerType == 'KID' :
            self.checkBalanceAndDeduct(reduceFare(KID_FARE), collectionSummary)
            collectionSummary.updateKidCount()
            collectionSummary.addToDiscount(reduceFare(KID_FARE))

        else :
            print('No Such PassengerType')

    #Passenger is Doing OneWay Journey, hence Actual fare will be deducted
    def deductForOneWayJourney(self, passengerType, collectionSummary) :
        #checking PassengerType
        if passengerType == 'ADULT' :
            self.checkBalanceAndDeduct(ADULT_FARE, collectionSummary)
            collectionSummary.updateAdultCount()
        elif passengerType == 'SENIOR_CITIZEN' :
            self.checkBalanceAndDeduct(SENIOR_CITIZEN_FARE, collectionSummary)
            collectionSummary.updateSeniorCitizenCount()
        elif passengerType == 'KID' :
            self.checkBalanceAndDeduct(KID_FARE, collectionSummary)
            collectionSummary.updateKidCount()
        else :
            print('No Such PassengerType') 

    
    
    def deductTravelCharges(self, travellingDestination, passengerType, collectionSummary) :
        
        if  self.getTravelDestination() != travellingDestination :            
            #if passenger doing OneWay Journey
            if self.isReturnJourney() == False :
                self.deductForOneWayJourney(passengerType, collectionSummary)
                self.updateIsReturnJourney(True)
            #if passenger doing Return Journey        
            else :
                self.deductForReturnJourney(passengerType, collectionSummary)
                self.updateIsReturnJourney(False)
            
            #updating travel Destination to check for same Source and Destination
            self.updateTravelDestination(travellingDestination)

        else :
            print ('Travel Source and Destination are Same !!!')




    def printDetails (self):
        print ('------------------------------')
        print (' ID : ' + self.passengerID)
        print (' Balance : ' + str(self.passengerBalance))
        print ('------------------------------')

