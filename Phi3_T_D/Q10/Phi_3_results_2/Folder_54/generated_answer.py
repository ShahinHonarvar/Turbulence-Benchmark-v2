def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[27:34], start=27) if x % 2 != 0]