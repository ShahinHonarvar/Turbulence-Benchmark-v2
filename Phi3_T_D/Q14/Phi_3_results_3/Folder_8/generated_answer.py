def find_second_smallest_num(lst):
    range_lst = lst[56:67]
    if len(range_lst) < 2:
        return None
    min1, min2 = (float('inf'), float('inf'))
    for num in range_lst:
        if num < min1:
            min1, min2 = (num, min1)
        elif num < min2:
            min2 = num
    return min2 if min2 != float('inf') else None