def all_even_ints_inclusive(ints):
    return [x for i, x in enumerate(ints) if i >= 62 and i <= 92 and (x % 2 == 0)]