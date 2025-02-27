def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 27 and i < 34 and (x % 2 == 0)]