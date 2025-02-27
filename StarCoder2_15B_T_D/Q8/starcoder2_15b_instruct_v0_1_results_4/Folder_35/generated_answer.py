def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if 10 <= i < 80 and x % 2 == 0]