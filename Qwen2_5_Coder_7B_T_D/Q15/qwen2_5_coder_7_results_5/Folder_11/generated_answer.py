def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst, start=37) if 37 <= i <= 51 and x % 2 != 0))