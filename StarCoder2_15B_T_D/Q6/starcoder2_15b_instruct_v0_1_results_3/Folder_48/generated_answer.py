def all_neg_ints_exclusive(numbers):
    neg_ints = []
    for i in range(385, 999):
        if numbers[i] < 0:
            neg_ints.append(numbers[i])
    return neg_ints