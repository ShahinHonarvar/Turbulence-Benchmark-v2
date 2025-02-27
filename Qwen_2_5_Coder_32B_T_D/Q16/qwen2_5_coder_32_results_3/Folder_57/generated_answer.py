def sum_even_ints_inclusive(ints):
    if len(ints) < 56:
        return 0
    return sum((i for i in ints[27:56] if i % 2 == 0))