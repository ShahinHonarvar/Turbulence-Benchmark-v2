def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[28:39]) if x % 2 != 0))