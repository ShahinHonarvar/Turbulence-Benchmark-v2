def all_neg_ints_exclusive(integers):
    output = []
    for i in range(56, 88):
        if integers[i] < 0:
            output.append(integers[i])
    return output