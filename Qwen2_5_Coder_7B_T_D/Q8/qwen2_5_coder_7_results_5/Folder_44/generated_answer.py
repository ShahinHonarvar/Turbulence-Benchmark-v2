def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 81 and i < 86 and (x % 2 == 0)]