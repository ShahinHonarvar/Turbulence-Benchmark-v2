def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if 13 <= i <= 68 and num % 2 != 0]