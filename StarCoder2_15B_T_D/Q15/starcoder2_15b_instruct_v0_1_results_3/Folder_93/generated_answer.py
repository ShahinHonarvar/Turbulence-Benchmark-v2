def sum_odd_ints_inclusive(ints):
    sum_odd_ints = 0
    for i in range(75, 95):
        if ints[i] % 2 == 1:
            sum_odd_ints += ints[i]
    return sum_odd_ints