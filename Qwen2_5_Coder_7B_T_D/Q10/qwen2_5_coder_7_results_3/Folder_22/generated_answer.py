def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 40 < i < 200 and num % 2 != 0]