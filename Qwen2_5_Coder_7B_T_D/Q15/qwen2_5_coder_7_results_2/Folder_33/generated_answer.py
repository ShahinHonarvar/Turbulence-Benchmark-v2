def sum_odd_ints_inclusive(numbers):
    return sum((n for i, n in enumerate(numbers) if i >= 667 and i <= 774 and (n % 2 != 0)))