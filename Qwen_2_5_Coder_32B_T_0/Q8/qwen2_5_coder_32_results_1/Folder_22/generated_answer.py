def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if 40 < i < 200 and x % 2 == 0]