def all_even_ints_inclusive(ints):
    result = []
    for i in range(31, 35):
        if ints[i] % 2 == 0:
            result.append(ints[i])
    return result