def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 43 < i < 99 and num % 2 != 0]