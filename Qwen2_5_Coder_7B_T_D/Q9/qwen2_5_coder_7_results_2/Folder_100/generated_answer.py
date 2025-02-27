def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if 42 <= i <= 68 and num % 2 != 0]