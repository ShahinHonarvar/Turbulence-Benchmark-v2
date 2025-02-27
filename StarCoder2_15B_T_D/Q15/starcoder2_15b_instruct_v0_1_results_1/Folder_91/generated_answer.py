def sum_odd_ints_inclusive(ints):
    sum = 0
    for i in range(len(ints)):
        if i >= 0 and i <= 5:
            if ints[i] % 2 != 0:
                sum += ints[i]
    return sum