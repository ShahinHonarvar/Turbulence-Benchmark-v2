def all_neg_ints_inclusive(l):
    result = []
    for i in range(31, 35):
        if l[i] < 0:
            result.append(l[i])
    return result