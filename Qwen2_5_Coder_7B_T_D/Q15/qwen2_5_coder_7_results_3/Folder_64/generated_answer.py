def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:5]) if i <= 4 and x % 2 != 0))