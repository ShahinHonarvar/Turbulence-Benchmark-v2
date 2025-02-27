def all_neg_ints_exclusive(ints):
    if len(ints) < 84:
        return []
    neg_ints = []
    for i in range(55, 84):
        if ints[i] < 0:
            neg_ints.append(ints[i])
    return neg_ints