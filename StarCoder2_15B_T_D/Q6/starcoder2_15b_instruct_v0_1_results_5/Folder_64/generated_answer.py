def all_neg_ints_exclusive(ints):
    result = []
    for i in range(len(ints)):
        if i >= 0 and i < 4:
            if ints[i] < 0:
                result.append(ints[i])
    return result