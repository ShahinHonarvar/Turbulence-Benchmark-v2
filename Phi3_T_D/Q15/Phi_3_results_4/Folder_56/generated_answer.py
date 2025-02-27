def sum_odd_ints_inclusive(intlist):
    return sum((i for i in intlist if i % 2 != 0))