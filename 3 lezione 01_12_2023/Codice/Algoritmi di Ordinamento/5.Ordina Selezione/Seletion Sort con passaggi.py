def Seletion_sort(input_list):
    i = 0
    
    for idx in range(len(input_list)): 
        min_idx = idx
        i += 1
        print(f'{i} passaggio ) : {input_list}')
        
        for j in range(idx + 1, len(input_list)):
            
            if input_list[min_idx] > input_list[j]:
                min_idx = j
                
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx] , input_list[idx]
        
list = [19,2,31,45,6,11,121,27]
Seletion_sort(list)