def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:9]) if i % 2 == 0 and x % 2 != 0]