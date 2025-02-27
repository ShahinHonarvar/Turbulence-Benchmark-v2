def all_pos_ints_inclusive(ints):
    result = []
    for i in range(1, 6):
        if ints[i] > 0:
            result.append(ints[i])
    return result