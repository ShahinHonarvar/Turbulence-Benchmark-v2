def all_odd_ints_exclusive(numbers):
    return [n for i, n in enumerate(numbers) if i > 81 and i < 86 and (n % 2 != 0)]