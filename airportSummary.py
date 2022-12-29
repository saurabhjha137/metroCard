class airportSummary :

    def __init__(self, collectionAmount = 0, discount = 0) :
        self.collectionAmount = collectionAmount
        self.discount = discount

    def addToCollection(self, passengerFare) :
        self.collectionAmount += passengerFare
    
    def addToDiscount(self, discountAmount) :
        self.discount += discountAmount

    def airportSummaryPrint (self) :
        print('TOTAL_COLLECTION AIRPORT '+ str(self.collectionAmount) + ' ' + str(self.discount))