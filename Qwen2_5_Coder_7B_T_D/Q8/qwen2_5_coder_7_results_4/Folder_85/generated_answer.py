def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 4 and i < 5 and (x % 2 == 0)]