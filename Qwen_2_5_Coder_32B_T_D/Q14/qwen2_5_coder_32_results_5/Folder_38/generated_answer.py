def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    sublist = lst[37:52]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sublist:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None