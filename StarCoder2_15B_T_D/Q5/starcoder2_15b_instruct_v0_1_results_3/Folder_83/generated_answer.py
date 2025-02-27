def all_neg_ints_inclusive(ints):
    result = []
    for i in range(len(ints)):
        if ints[i] < 0 and 90 <= i <= 200:
            result.append(ints[i])
    return result