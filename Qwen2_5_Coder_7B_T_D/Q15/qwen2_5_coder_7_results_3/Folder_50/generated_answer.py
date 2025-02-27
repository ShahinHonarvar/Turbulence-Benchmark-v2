def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if 70 <= i <= 84 and n % 2 != 0))