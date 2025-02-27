def all_neg_ints_inclusive(lst):
    if not lst:
        return []
    neg_ints = []
    for i, num in enumerate(lst):
        if num < 0 and 25 <= i <= 87:
            neg_ints.append(num)
    return neg_ints