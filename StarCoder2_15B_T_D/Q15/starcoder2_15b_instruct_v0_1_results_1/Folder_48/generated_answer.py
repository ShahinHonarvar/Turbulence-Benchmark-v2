def sum_odd_ints_inclusive(ints):
    sum_odd = 0
    for i in range(533, 606):
        if ints[i] % 2 != 0:
            sum_odd += ints[i]
    return sum_odd