def find_second_largest_num(lst):
    if len(lst) < 88:
        return None
    sub_lst = lst[25:88]
    if len(sub_lst) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_lst:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None