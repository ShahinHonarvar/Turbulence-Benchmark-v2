def all_neg_ints_inclusive(lst):
    if not any((x < 0 for x in lst)):
        return []
    neg_ints = []
    for i in range(5):
        if lst[i] < 0:
            neg_ints.append(lst[i])
    return neg_ints