def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 43 and i < 99 and (num % 2 == 0)]