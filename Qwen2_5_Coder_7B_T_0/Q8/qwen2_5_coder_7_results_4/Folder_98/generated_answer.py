def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 0 and i < 7 and (x % 2 == 0)]