def find_second_smallest_num(lst):
    if len(lst) < 89:
        return None
    sublist = lst[22:89]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None