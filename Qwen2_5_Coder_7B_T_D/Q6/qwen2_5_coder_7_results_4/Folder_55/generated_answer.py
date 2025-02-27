def all_neg_ints_exclusive(numbers):
    return [num for idx, num in enumerate(numbers) if idx > 0 and idx < 10 and (num < 0)]