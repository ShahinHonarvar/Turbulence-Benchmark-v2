def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < i < 7 and x % 2 == 0]