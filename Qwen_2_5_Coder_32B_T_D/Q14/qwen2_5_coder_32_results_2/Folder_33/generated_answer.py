def find_second_smallest_num(lst):
    if len(lst) < 747:
        return None
    sublist = lst[262:747]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for number in sublist:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None