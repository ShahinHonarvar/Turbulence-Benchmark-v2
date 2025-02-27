def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[20:36], start=20) if x % 2 != 0]