def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[18:60], start=18) if x % 2 != 0]