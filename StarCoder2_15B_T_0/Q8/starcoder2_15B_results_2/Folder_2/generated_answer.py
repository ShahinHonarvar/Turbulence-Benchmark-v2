def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 36 and i < 52 and (x % 2 == 0)]