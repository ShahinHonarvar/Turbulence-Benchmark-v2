def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(5):
        if ints[i] % 2 == 1:
            sum += ints[i]
    return sum