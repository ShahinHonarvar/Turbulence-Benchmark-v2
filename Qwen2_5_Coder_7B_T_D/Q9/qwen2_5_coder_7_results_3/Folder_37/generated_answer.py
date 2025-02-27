def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if 1 <= i <= 5 and num % 2 != 0]