def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 15 < i < 40 and x % 2 == 0]