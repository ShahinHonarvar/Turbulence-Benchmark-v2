def all_neg_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 12 <= i <= 92 and num < 0]