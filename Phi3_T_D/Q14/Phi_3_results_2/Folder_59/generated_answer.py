def find_second_smallest_num(lst):
    if len(lst) <= 9:
        LST = lst
    else:
        LST = lst[:10]
    if len(set(LST)) < 2:
        return None
    first_smallest = min(LST)
    second_smallest = float('inf')
    for num in LST:
        if num > first_smallest and num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None