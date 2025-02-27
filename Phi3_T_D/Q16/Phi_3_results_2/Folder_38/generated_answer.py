def sum_even_ints_inclusive(ints):
    even_sum = sum((x for x in ints[22:64] if x % 2 == 0))
    return even_sum