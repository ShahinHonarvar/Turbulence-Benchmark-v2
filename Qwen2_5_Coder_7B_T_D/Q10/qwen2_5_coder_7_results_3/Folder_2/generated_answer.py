def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 37 <= i <= 51 and x % 2 != 0]