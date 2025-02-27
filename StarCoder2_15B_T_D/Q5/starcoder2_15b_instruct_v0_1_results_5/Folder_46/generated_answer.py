def all_neg_ints_inclusive(lst):
    neg_ints = []
    for i, num in enumerate(lst):
        if num < 0 and 30 <= i <= 87:
            neg_ints.append(num)
    return neg_ints