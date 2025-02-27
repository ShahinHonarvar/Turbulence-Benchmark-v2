def sum_even_ints_inclusive(ints):
    return sum((x for x in ints[0:9] if x % 2 == 0))