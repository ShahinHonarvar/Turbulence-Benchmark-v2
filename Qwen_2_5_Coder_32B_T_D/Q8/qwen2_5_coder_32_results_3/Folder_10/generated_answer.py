def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 48 < i < 74 and x % 2 == 0]