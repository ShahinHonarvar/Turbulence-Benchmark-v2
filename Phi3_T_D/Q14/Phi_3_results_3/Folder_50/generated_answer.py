def find_second_smallest_num(lst):
    second_smallest = None
    for i in range(42, 69):
        if lst[i] != min(lst[42:69]) and (second_smallest is None or lst[i] < second_smallest):
            second_smallest = lst[i]
    return second_smallest