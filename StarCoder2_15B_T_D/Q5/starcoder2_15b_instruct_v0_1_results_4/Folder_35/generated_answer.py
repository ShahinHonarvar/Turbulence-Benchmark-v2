def all_neg_ints_inclusive(numbers):
    neg_ints = []
    for i in range(30, 49):
        if numbers[i] < 0:
            neg_ints.append(numbers[i])
    return neg_ints