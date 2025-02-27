def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst, start=1) if 18 < i < 38 and x % 2 == 0]