def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 41 < i < 69 and x % 2 == 0]