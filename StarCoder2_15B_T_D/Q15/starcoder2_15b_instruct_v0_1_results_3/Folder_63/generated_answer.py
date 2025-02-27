def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(len(ints)):
        if i >= 22 and i <= 88 and (ints[i] % 2 != 0):
            sum += ints[i]
    return sum