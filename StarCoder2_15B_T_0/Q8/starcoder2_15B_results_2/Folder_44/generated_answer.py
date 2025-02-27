def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 81 and i < 86 and (x % 2 == 0)]