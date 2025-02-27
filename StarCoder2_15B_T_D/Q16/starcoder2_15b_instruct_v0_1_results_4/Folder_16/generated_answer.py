def sum_even_ints_inclusive(ints):
    ints = ints[33:37]
    return sum((x for x in ints if x % 2 == 0))