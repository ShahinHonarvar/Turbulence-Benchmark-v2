def find_second_smallest_num(lst):
    if len(lst) < 77:
        return None
    sublist = lst[37:77]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None