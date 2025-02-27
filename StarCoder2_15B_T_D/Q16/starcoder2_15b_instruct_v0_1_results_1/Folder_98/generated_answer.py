def sum_even_ints_inclusive(ints):
    return sum((i for i in ints[0:7] if i % 2 == 0))