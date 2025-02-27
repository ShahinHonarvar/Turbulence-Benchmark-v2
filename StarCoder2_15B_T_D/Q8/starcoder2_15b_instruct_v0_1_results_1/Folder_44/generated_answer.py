def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 80 and i < 86 and (num % 2 == 0)]