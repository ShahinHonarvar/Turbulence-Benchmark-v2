def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 50 < i < 92 and x % 2 == 0]