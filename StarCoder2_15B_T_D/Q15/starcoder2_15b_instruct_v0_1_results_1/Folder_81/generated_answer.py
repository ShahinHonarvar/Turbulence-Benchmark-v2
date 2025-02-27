def sum_odd_ints_inclusive(ints):
    result = 0
    for i in range(10, 101):
        if ints[i] % 2 != 0:
            result += ints[i]
    return result