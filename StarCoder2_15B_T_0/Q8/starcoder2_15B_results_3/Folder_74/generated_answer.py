def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 13 <= i < 70 and x % 2 == 0]