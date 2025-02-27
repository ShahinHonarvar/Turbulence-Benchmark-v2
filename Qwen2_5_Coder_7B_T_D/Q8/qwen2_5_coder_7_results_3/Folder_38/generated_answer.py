def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 15 and i < 40 and (num % 2 == 0)]