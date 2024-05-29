def merge(left_list, right_list):
    res = []
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        if left_list[0] > right_list[0]:
            res.append(right_list[0])
            left_list.remove(right_list[0])

list = [19,2,31,45,6,11,121,27]
merge(list)