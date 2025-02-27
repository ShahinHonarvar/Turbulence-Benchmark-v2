def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 78 and i < 93 and (x % 2 == 0)]