def all_neg_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 20 <= i <= 200 and num < 0]