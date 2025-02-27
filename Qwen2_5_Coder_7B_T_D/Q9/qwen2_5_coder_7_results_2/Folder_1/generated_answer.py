def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if 31 <= i <= 72 and num % 2 != 0]