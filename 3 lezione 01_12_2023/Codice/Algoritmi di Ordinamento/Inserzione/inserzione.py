def insertion_sort(InputList):
    for i in range (1,len(InputList)):
        j = i-1
        nxt_element = InputList[i]

#Compara l'elemento attuale col successivo

    while(InputList[j] > nxt_element) and (j >= 0):
        InputList[j+1] = InputList[j]
        j = j-1
    InputList[j + 1] = nxt_element

InputList=[19,2,31,45,6,11,121,27]
insertion_sort(InputList)
print(InputList)