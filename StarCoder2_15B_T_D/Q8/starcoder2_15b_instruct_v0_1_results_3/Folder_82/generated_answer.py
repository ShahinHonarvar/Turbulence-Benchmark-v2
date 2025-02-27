def all_even_ints_exclusive(ints):
    return [n for i, n in enumerate(ints) if 20 < i < 200 and n % 2 == 0]