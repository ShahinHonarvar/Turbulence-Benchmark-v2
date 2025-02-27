def find_second_smallest_num(lst):
    if len(lst) < 41 or 81 >= len(lst):
        return None
    second_smallest = None
    smallest = None
    for i in range(40, 81):
        if smallest is None or lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif (second_smallest is None or lst[i] < second_smallest) and lst[i] != smallest:
            second_smallest = lst[i]
    return second_smallest