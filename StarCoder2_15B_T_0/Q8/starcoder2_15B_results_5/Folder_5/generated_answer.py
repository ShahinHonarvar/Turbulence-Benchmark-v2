def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i % 2 == 0 and 2 <= i < 7]