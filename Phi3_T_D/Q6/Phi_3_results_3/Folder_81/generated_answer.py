def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers[10:100], start=10) if num < 0]