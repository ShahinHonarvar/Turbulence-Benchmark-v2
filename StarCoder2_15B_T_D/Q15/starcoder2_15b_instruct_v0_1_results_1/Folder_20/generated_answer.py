def sum_odd_ints_inclusive(ints):
    odd_ints = [i for i in ints if i % 2 == 1]
    if len(odd_ints) > 66:
        return sum(odd_ints[56:67])
    else:
        return 0