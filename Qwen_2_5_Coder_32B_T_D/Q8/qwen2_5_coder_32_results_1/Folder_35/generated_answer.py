def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 10 < i < 79 and x % 2 == 0]