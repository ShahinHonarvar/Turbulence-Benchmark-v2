def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 36 and i < 54 and (x % 2 == 0)]