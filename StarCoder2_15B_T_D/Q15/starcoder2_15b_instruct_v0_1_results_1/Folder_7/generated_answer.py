def sum_odd_ints_inclusive(ints):
    return sum((int for int in ints[661:925] if int % 2 == 1))