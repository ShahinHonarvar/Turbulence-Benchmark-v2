def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 100 < i < 102 and x % 2 == 0]