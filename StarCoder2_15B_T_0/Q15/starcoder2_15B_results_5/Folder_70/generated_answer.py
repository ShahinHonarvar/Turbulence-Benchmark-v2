def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(28, 33):
        if ints[i] % 2 != 0:
            sum += ints[i]
    return sum