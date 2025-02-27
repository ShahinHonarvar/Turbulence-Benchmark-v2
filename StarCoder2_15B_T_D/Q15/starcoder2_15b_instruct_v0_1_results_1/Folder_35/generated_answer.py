def sum_odd_ints_inclusive(ints):
    odd_ints = [i for i in ints[30:50] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0