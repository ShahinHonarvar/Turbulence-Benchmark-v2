def sum_even_ints_inclusive(ints):
    return sum((int for int in ints[0:9] if int % 2 == 0))