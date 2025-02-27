def all_even_ints_inclusive(ints):
    result = []
    for i in range(26, 53):
        if ints[i] % 2 == 0:
            result.append(ints[i])
    return result