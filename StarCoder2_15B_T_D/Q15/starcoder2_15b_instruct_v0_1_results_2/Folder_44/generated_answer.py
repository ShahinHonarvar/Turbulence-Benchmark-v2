def sum_odd_ints_inclusive(ints):
    total = 0
    for i in range(13, 69):
        if ints[i] % 2 == 1:
            total += ints[i]
    return total