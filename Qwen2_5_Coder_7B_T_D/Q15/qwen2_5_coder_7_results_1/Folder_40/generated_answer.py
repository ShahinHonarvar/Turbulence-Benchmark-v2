def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:3]) if i in [0, 2] and x % 2 != 0))