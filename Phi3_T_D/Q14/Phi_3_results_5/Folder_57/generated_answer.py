def find_second_smallest_num(lst):
    applicable_lst = lst[20:31]
    if len(applicable_lst) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in applicable_lst:
        if num < min1:
            min1, min2 = (num, min1)
        elif num < min2:
            min2 = num
    return min2