def sum_odd_ints_inclusive(ints):
    running_total = 0
    for i in range(1, 9):
        if ints[i] % 2 != 0:
            running_total += ints[i]
    return running_total