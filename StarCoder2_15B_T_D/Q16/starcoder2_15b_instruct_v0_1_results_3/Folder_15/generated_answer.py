def sum_even_ints_inclusive(ints):
    return sum((int for int in ints[:4] if int % 2 == 0))