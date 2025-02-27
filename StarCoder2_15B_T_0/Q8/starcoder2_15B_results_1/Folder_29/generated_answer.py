def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 48 and i < 76 and (x % 2 == 0)]