def all_neg_ints_exclusive(numbers):
    neg_ints = []
    for i, num in enumerate(numbers):
        if num < 0 and 361 <= i < 643:
            neg_ints.append(num)
    return neg_ints