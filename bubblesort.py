myList= [22, 5, 9, 33, 1, 7, 44, 8]
def ascendingBubbleSort(unsortedList):
    length = len(unsortedList) - 1
    element = 0
    while element < length:
        if unsortedList[element] < unsortedList[element + 1]:
            hold = unsortedList[element + 1]
            unsortedList[element + 1] = unsortedList[element]
            unsortedList[element] = hold
            element = 0
        else:
            element = element + 1
    return (unsortedList)

print ascendingBubbleSort(myList)

