def all_neg_ints_exclusive(ints):
    result = []
    for i in range(len(ints)):
        if i < 0 or i >= 8:
            continue
        if ints[i] < 0:
            result.append(ints[i])
    return result