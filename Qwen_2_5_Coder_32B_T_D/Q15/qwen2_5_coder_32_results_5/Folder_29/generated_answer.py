def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 59 and i <= 97 and (x % 2 != 0)))