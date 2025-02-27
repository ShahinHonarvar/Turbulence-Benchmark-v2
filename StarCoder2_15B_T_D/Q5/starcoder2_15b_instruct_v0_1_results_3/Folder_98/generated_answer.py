def all_neg_ints_inclusive(ints):
    has_neg = False
    for i in ints:
        if i < 0:
            has_neg = True
            break
    if not has_neg:
        return []
    neg_ints = []
    for i in ints[:7]:
        if i < 0:
            neg_ints.append(i)
    return neg_ints