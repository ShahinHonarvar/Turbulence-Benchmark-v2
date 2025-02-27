def sum_even_ints_inclusive(ints):
    result = 0
    for i in range(8):
        if ints[i] % 2 == 0:
            result += ints[i]
    return result