def all_even_ints_exclusive(numbers):
    return [n for i, n in enumerate(numbers) if n % 2 == 0 and 0 < i < 5]