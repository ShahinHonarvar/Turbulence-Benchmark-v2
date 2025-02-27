def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 10 < i < 76 and num % 2 != 0]