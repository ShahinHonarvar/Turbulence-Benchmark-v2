def sum_odd_ints_inclusive(lst):
    start_index = 23
    end_index = 23
    return sum((x for x in lst[start_index:end_index + 1] if x % 2 != 0))