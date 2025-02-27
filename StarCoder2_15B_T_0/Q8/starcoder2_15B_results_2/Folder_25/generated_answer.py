def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 41 and i < 69 and (x % 2 == 0)]