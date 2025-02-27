def all_neg_ints_inclusive(lst):
    output = []
    for i in range(17, 79):
        if lst[i] < 0:
            output.append(lst[i])
    return output