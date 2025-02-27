def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 15 < i < 40 and num % 2 == 0]