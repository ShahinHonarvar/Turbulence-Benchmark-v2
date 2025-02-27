def all_odd_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i % 2 == 1 and 23 < i < 45]