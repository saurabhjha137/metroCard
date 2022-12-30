from metroCardPassengers import metroCardPassengers
from airportSummary import airportSummary
from centralSummary import centralSummary

def checkInActions (passengerList, inputString) :
    passengerID = inputString.split()[1]
    passengerType = inputString.split()[2]
    travellingSource = inputString.split()[3]

    if  travellingSource == 'CENTRAL' :
        travellingDestination = 'AIRPORT'
        for passenger in passengerList :
            if passengerID == passenger.getPassengerID() :
                passenger.deductTravelCharges(travellingDestination, passengerType, centralCollectionSummary)
                break
    else : 
        travellingDestination = 'CENTRAL'
        for passenger in passengerList :
            if passengerID == passenger.getPassengerID() :
                passenger.deductTravelCharges(travellingDestination, passengerType, airportCollectionSummary)
                break

if __name__ == '__main__':
    
    passengerList = []
    airportCollectionSummary =  airportSummary ()
    centralCollectionSummary =  centralSummary ()

    file = open('sampleIOfile2.txt', 'r+')
    # file = open(sys.argv[1], 'r+')
    
    for inputString in file.readlines():
        
        action = inputString.split()[0]
        if action == "BALANCE":
            passengerID = inputString.split()[1]
            passengerBalance = inputString.split()[2]
            newPassenger = metroCardPassengers(passengerID, passengerBalance)
            passengerList.append(newPassenger)

        elif action == "CHECK_IN":
            checkInActions(passengerList, inputString)

        elif action == "PRINT_SUMMARY":
            centralCollectionSummary.centralSummaryPrint()
            airportCollectionSummary.airportSummaryPrint()

    #for passenger in passengerList :
    #    passenger.printDetails()

    file.close()