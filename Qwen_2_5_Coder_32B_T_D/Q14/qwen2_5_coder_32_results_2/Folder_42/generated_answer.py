def find_second_smallest_num(lst):
    if len(lst) < 98:
        return None
    sub_list = lst[21:98]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None