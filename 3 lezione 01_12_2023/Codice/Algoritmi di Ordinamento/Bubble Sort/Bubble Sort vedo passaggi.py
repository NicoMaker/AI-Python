def bubblesort (list):
    i = 0
# Swap the elements to arrange in order
    for iter_num in range (len(list) -1,0, -1): 
        i += 1
        print(f'{i} passaggio ) : {list}')
        
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

print(list)
list = [19,2,31,45,6,11,121,27]
bubblesort (list)