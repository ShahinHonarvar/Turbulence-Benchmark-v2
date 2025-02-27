def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i, num in enumerate(int_list):
        if num < 0 and 28 <= i <= 32:
            neg_ints.append(num)
    return neg_ints