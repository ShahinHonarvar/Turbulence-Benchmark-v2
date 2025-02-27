def sum_odd_ints_inclusive(ints):
    total = 0
    for i in range(15, 40):
        if ints[i] % 2 == 1:
            total += ints[i]
    return total