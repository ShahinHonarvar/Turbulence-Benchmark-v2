def all_even_ints_exclusive(lst):
    return [x for i, x in enumerate(lst) if i > 38 and i < 77 and (x % 2 == 0)]