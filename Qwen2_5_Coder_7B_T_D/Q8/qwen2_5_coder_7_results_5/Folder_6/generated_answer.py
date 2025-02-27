def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 86 and i < 99 and (x % 2 == 0)]