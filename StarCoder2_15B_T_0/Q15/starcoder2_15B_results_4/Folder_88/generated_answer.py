def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(4, 9):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum