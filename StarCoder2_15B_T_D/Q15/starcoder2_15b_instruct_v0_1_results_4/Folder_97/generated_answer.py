def sum_odd_ints_inclusive(ints):
    result = 0
    for i in range(40, 81):
        if ints[i] % 2 == 1:
            result += ints[i]
    return result