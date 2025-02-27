def sum_even_ints_inclusive(ints):
    even_ints = [x for x in ints[43:87] if x % 2 == 0]
    return sum(even_ints)