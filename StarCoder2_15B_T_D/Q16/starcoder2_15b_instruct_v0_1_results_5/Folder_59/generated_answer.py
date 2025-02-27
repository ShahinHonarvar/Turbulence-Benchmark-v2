def sum_even_ints_inclusive(ints):
    return sum((i for i in ints[:10] if i % 2 == 0))