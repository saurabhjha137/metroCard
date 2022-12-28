
if __name__ == '__main__':
    # initializes existing tree
    familyTree = CreateFamilyTree()
    familyHead = familyTree.make_family_tree()
    # passes familyHead i.e. King Shan to process results based on input
    inputTask = InputTaskFunctions(familyHead)
    file = open('myfile.txt', 'r+')
    # file = open(sys.argv[1], 'r+')
    # -------- Below block adds_child and gets_relation ------- #
    for inputString in file.readlines():
        
        action = inputString.split()[0]
        if action == "ADD_CHILD":
            motherName = inputString.split()[1]
            childName = inputString.split()[2]
            childGender = inputString.split()[3]
            inputTask.add_input_child(motherName, childName,
                                   childGender)

        elif action == "GET_RELATIONSHIP":
            name = inputString.split()[1]
            relation = inputString.split()[2]
            inputTask.get_relationship_of_member(name, relation)

    file.close()