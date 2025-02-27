def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst, start=34) if 34 <= i <= 55 and x % 2 != 0))