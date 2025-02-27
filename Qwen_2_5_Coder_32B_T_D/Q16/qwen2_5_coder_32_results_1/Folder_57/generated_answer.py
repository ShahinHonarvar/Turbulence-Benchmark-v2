def sum_even_ints_inclusive(ints):
    if len(ints) < 56:
        return 0
    return sum((x for x in ints[27:56] if x % 2 == 0))