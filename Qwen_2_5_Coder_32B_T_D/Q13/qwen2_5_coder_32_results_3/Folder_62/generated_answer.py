def find_second_largest_num(lst):
    if len(lst) < 100:
        return None
    sub_list = lst[91:100]
    if len(sub_list) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for num in sub_list:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second if second != float('-inf') else None