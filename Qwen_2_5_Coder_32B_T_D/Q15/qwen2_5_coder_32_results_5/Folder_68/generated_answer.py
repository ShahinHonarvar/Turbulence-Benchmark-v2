def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:9]) if i < len(lst) and x % 2 != 0))