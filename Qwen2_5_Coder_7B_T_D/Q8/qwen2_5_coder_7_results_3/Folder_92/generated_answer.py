def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 0 < i < 2 and x % 2 == 0]