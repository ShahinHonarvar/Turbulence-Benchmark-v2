def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 25 and i < 80 and (num % 2 == 0)]