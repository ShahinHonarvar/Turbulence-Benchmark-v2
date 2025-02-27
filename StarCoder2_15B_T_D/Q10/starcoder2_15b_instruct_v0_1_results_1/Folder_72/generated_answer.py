def all_odd_ints_exclusive(ints):
    result = []
    for i in range(56, 88):
        if ints[i] % 2 == 1:
            result.append(ints[i])
    return result