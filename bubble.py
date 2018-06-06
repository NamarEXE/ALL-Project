def bubble(badList):
    length = len(badList) - 1
    element = 0
    while element < length:
        if badList[element] > badList[element + 1]:
            hold = badList[element + 1]
            badList[element + 1] = badList[element]
            badList[element] = hold
            element = 0
            print badList
        else:
            element = element + 1

print bubble(mylist)




def bubble(badList):
    length = len(badList) - 1
    unsorted = True
    while unsorted:
        unsorted = False
        for element in range(0,length):
            #unsorted = False
            if badList[element] > badList[element + 1]:
                 hold = badList[element + 1]
                 badList[element + 1] = badList[element]
                 badList[element] = hold
                 unsorted = True
                 #print badList
             #else:
                 #unsorted = True

     return badList

    http://stackoverflow.com/questions/895371/bubble-sort-homework
    
