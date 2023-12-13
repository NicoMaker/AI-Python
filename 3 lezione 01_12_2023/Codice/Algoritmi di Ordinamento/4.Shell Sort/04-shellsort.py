def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
                print(input_list)
            input_list[j] = temp

# Reduce the gap for the next element

        gap = gap//2

list = [19,2,31,45,6,11,121]
print('shellsort')
shellSort(list)
print(list)
lista2 = [119,12,131,245,56,311,121,36]
print('shellsort')
shellSort(lista2)
print(lista2)