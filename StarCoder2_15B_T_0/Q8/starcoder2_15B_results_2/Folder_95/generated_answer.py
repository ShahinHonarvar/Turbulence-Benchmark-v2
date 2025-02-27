def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 25 <= i < 80 and x % 2 == 0]