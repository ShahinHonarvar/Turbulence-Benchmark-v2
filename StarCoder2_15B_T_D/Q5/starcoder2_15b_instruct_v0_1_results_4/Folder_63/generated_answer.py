def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i, num in enumerate(int_list):
        if num < 0 and 22 <= i <= 88:
            neg_ints.append(num)
        else:
            continue
    if not neg_ints:
        return []
    return neg_ints