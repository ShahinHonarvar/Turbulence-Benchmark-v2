def find_second_largest_num(lst):
    if len(lst) < 33:
        return None
    sublist = lst[28:33]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sublist:
        if number > first:
            second = first
            first = number
        elif number > second:
            second = number
    return second if second != float('-inf') else None