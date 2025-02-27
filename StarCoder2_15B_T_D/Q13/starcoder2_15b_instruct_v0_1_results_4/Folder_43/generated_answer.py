def find_second_largest_num(lst):
    second_largest = None
    for i in range(68, 87):
        if lst[i] > second_largest:
            second_largest = lst[i]
    return second_largest