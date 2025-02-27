def find_second_largest_num(lst):
    if len(lst) < 8:
        return None
    first, second = (float('-inf'), float('-inf'))
    for i in range(8):
        if lst[i] > first:
            second = first
            first = lst[i]
        elif lst[i] > second:
            second = lst[i]
    return second if second != float('-inf') else None