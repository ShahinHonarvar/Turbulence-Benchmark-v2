def all_odd_ints_inclusive(numbers):
    return [n for i, n in enumerate(numbers) if 13 <= i <= 68 and n % 2 != 0]