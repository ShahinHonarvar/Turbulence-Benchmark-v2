def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 639 <= i <= 975 and x % 2 != 0))