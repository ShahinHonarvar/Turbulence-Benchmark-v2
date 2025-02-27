def all_neg_ints_exclusive(integers):
    result = []
    for i in range(598, 767):
        if integers[i] < 0:
            result.append(integers[i])
    return result