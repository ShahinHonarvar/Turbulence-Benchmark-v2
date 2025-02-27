def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(43, 87):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum