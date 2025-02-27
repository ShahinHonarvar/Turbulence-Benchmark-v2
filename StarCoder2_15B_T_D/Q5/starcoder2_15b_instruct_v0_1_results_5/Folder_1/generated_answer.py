def all_neg_ints_inclusive(int_list):
    neg_ints = []
    for i, num in enumerate(int_list):
        if num < 0 and 31 <= i <= 72:
            neg_ints.append(num)
    return neg_ints