def find_second_smallest_num(lst):
    if len(lst) < 557:
        return None
    sub_lst = lst[209:557]
    if len(sub_lst) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_lst:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None