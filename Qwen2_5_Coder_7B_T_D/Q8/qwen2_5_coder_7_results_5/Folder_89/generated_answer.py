def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 51 and i < 76 and (x % 2 == 0)]