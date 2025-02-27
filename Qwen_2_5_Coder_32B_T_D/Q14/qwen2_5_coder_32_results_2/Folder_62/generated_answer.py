def find_second_smallest_num(lst):
    if len(lst) < 67 or not isinstance(lst, list):
        return None
    sub_lst = lst[10:67]
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