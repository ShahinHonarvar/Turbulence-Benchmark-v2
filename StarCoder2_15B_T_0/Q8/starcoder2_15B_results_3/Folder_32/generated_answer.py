def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 11 <= i < 76 and x % 2 == 0]