def all_odd_ints_inclusive(ints):
    result = []
    for i in range(33, 37):
        if ints[i] % 2 == 1:
            result.append(ints[i])
    return result