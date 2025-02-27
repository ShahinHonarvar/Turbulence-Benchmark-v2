def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 38 and i < 77 and (x % 2 == 0)]