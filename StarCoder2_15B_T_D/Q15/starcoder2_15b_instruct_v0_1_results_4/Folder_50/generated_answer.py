def sum_odd_ints_inclusive(ints):
    total = 0
    for i in range(70, 85):
        if ints[i] % 2 == 1:
            total += ints[i]
    return total