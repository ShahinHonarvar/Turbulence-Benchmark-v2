def sum_odd_ints_inclusive(ints):
    return sum((x for x in ints[0:10] if x % 2 == 1))