def all_neg_ints_exclusive(lst):
    neg_ints = []
    for i, num in enumerate(lst):
        if num < 0 and 55 <= i < 84:
            neg_ints.append(num)
    return neg_ints