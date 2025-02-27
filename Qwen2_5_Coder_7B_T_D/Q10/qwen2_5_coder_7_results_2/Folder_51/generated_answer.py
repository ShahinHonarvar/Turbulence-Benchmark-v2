def all_odd_ints_exclusive(lst):
    return [n for i, n in enumerate(lst) if 6 < i < 9 and n % 2 != 0]