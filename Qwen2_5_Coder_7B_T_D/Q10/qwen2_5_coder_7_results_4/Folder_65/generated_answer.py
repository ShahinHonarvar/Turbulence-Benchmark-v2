def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst[42:88]) if i % 2 != 0 and x % 2 != 0]