def all_odd_ints_inclusive(ints):
    result = []
    for i in range(len(ints)):
        if i >= 82 and i <= 86 and (ints[i] % 2 == 1):
            result.append(ints[i])
    return result