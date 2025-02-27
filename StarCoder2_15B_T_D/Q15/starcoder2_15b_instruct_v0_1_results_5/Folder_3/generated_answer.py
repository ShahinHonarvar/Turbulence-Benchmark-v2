def sum_odd_ints_inclusive(ints):
    ints = ints[62:93]
    return sum([n for n in ints if n % 2 != 0])