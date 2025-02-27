def all_odd_ints_inclusive(ints):
    result = []
    for i in range(len(ints)):
        if i >= 0 and i <= 5:
            if ints[i] % 2 == 1:
                result.append(ints[i])
    return result