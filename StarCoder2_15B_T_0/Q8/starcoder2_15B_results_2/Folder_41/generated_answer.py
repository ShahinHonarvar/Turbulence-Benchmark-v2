def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 8 and i < 9 and (x % 2 == 0)]