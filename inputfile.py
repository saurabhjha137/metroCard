from metroCardMembers import metroCardMembers


if __name__ == '__main__':
    
    file = open('myfile.txt', 'r+')
    # file = open(sys.argv[1], 'r+')
    # -------- Below block adds_child and gets_relation ------- #
    for inputString in file.readlines():
        
        action = inputString.split()[0]
        if action == "BALANCE":
            memberID = inputString.split(' ')[1]
            memberBalance = inputString.split(' ')[2]
            memberType = inputString.split(' ')[3]
            newMember = metroCardMembers(memberID, memberBalance, memberID)
            newMember.printDetails()

        elif action == "CHECK_IN":
            print ('Checkin')
        elif action == "PRINT_SUMMARY":
            print ('Summmary')
    file.close()