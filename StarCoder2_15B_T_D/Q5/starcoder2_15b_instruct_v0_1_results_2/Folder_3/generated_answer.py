def all_neg_ints_inclusive(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    neg_ints = []
    for i, num in enumerate(lst):
        if num < 0 and 62 <= i <= 92:
            neg_ints.append(num)
    return neg_ints