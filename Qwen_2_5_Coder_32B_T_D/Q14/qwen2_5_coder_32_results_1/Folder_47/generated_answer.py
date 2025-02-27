def find_second_smallest_num(lst):
    if len(lst) < 64:
        return None
    sub_lst = lst[22:64]
    if len(sub_lst) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sub_lst:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None