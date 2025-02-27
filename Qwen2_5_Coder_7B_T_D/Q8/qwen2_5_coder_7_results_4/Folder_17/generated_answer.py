def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 62 and i < 96 and (x % 2 == 0)]