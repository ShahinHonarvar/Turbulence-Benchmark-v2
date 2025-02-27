def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if x % 2 == 0 and 0 < i < 2]