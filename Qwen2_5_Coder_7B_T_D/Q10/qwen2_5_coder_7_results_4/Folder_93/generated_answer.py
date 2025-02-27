def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 19 < i < 94 and num % 2 != 0]