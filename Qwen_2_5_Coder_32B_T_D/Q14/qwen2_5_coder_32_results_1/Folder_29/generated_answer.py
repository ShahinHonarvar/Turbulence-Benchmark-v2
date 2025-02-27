def find_second_smallest_num(lst):
    if len(lst) < 99:
        return None
    sliced_list = lst[55:99]
    if len(sliced_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sliced_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None