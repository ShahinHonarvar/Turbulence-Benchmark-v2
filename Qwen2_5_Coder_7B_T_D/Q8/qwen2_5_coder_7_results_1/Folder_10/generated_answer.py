def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 48 and i < 74 and (num % 2 == 0)]