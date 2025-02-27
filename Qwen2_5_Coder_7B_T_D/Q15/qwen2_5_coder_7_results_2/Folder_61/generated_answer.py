def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:8]) if i in range(8) and x % 2 != 0))