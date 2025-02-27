def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:11]) if i < 11 and x % 2 != 0))