def sum_odd_ints_inclusive(lst):
    if len(lst) <= 57:
        return 0
    start_index = 56
    end_index = 57
    sum_odd = sum((x for x in lst[start_index:end_index + 1] if x % 2 != 0))
    return sum_odd