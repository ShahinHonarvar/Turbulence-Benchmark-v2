def find_second_smallest_num(lst):
    start, end = (6, len(lst) - 1 if len(lst) > 6 else 5)
    if start > end:
        return None
    second_smallest = None
    for i in range(start, end + 1):
        if second_smallest is None or (lst[i] > lst[start] and lst[i] < second_smallest):
            second_smallest = lst[i]
    return second_smallest