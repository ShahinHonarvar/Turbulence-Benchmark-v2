def all_odd_ints_inclusive(numbers):
    return [num for idx, num in enumerate(numbers) if 13 <= idx <= 68 and num % 2 != 0]