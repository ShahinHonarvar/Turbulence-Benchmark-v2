def all_neg_ints_exclusive(ints):
    neg_ints = []
    for i in range(len(ints)):
        if i >= 0 and i < 7 and (ints[i] < 0):
            neg_ints.append(ints[i])
    return neg_ints