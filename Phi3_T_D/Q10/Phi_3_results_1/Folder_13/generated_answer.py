def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[73:83], start=73) if x % 2 != 0]