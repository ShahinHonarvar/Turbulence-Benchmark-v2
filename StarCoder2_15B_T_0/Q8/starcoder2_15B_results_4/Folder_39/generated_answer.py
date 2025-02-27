def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 43 and i < 99 and (x % 2 == 0)]