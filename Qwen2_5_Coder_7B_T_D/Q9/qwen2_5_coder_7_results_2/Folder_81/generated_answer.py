def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 10 <= i <= 100 and x % 2 != 0]