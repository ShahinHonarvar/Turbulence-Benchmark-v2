def all_pos_ints_inclusive(ints):
    result = []
    for i in range(len(ints)):
        if 28 <= i <= 32 and ints[i] > 0:
            result.append(ints[i])
    return result