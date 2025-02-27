def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[37:52]) if i % 2 == 0 and x % 2 != 0))