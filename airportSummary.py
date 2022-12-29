class airportSummary :

    def __init__(self, collectionAmount = 0, discount = 0) :
        self.collectionAmount = collectionAmount
        self.discount = discount

    def addToCollection(self, passengerFare) :
        self.collectionAmount += passengerFare
        
    def airportSummary (self) :
        print('')