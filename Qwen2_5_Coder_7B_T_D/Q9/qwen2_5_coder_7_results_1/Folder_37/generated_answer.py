def all_odd_ints_inclusive(numbers):
    return [n for i, n in enumerate(numbers) if 1 <= i <= 5 and n % 2 != 0]