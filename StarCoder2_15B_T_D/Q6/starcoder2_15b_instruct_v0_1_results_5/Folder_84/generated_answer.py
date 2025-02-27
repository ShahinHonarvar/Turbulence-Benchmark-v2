def all_neg_ints_exclusive(ints):
    neg_ints = []
    for i, num in enumerate(ints):
        if num < 0 and 50 <= i < 92:
            neg_ints.append(num)
    return neg_ints