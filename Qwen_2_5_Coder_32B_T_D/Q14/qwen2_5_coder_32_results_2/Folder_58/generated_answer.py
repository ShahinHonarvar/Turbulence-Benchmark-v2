def find_second_smallest_num(lst):
    if len(lst) < 371:
        return None
    sub_list = lst[310:371]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None