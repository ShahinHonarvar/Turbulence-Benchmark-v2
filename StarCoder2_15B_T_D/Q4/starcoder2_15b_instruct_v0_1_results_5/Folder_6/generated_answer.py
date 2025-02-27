def all_pos_ints_exclusive(ints):
    result = []
    for i in range(len(ints)):
        if i >= 86 and i < 99:
            if ints[i] > 0:
                result.append(ints[i])
    return result