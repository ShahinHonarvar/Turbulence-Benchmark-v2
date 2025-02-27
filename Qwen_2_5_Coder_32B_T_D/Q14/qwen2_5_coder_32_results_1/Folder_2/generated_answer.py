def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    sublist = lst[43:87]
    if len(sublist) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None