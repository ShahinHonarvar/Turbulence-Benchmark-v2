def find_second_largest_num(lst):
    if len(lst) < 51:
        return None
    sublist = lst[22:51]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None