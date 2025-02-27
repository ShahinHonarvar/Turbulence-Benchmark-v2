def all_odd_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:9]) if i <= 8 and x % 2 != 0]