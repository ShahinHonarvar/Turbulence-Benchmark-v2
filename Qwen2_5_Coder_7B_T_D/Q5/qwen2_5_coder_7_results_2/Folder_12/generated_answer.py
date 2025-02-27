def all_neg_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 14 <= i <= 64 and num < 0]