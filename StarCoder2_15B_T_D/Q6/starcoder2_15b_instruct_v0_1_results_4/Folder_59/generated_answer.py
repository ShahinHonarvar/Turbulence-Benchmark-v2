def all_neg_ints_exclusive(numbers):
    neg_ints = []
    for i in range(len(numbers)):
        if numbers[i] < 0 and 0 <= i < 9:
            neg_ints.append(numbers[i])
    return neg_ints