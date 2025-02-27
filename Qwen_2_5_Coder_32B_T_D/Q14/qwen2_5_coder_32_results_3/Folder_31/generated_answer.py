def find_second_smallest_num(lst):
    if len(lst) < 94:
        return None
    sub_lst = lst[29:94]
    if len(sub_lst) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_lst:
        if num < first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None