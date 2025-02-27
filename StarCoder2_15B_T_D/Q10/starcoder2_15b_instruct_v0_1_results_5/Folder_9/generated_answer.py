def all_odd_ints_exclusive(ints):
    result = []
    for i in range(len(ints)):
        if i >= 70 and i < 71:
            if ints[i] % 2 == 1:
                result.append(ints[i])
    return result