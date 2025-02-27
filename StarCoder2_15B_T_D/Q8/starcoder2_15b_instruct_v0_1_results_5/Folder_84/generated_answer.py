def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 50 and i < 92 and (num % 2 == 0)]