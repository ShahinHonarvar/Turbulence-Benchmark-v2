def all_even_ints_exclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 70 and i < 98 and (x % 2 == 0)]