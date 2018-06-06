myList= [22, 5, 9, 33, 1, 7, 44, 8]
def ascendingQuickSort(unsortedList):
    less = []
    equal = []
    greater = []

    if len(unsortedList) > 1:
        pivot = unsortedList[0]
        for x in unsortedList:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        print(less, equal, greater)
        return ascendingQuickSort(less)+equal+ascendingQuickSort(greater)
    
    else:  
        return unsortedList

print (ascendingQuickSort(myList))
