def find_second_largest_num(lst):
    if len(lst) < 94:
        return None
    sublist = lst[29:94]
    if len(sublist) < 2:
        return None
    first, second = (float('-inf'), float('-inf'))
    for number in sublist:
        if number > first:
            first, second = (number, first)
        elif number > second:
            second = number
    return second if second != float('-inf') else None