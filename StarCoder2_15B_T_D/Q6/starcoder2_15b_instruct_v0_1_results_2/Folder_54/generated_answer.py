def all_neg_ints_exclusive(ints):
    output = []
    for i in range(27, 34):
        if ints[i] < 0:
            output.append(ints[i])
    return output