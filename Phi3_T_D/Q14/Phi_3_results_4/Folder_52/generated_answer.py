def find_second_smallest_num(lst):
    start, end = (64, min(66, len(lst) - 1))
    second_smallest = None
    for i in range(start, end + 1):
        if i == start:
            second_smallest = max(lst[start], lst[start + 1])
        else:
            second_smallest = min(second_smallest, lst[i]) if second_smallest is not None else lst[i]
    return second_smallest