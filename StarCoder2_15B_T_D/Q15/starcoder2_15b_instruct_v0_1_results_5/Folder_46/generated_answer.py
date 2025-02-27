def sum_odd_ints_inclusive(ints):
    odd_ints = [i for i in ints[30:88] if i % 2 == 1]
    return sum(odd_ints)