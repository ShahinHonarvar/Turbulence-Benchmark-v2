def all_odd_ints_exclusive(numbers):
    return [n for i, n in enumerate(numbers) if i > 2 and i < 7 and (n % 2 != 0)]