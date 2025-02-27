def all_even_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 31 and i <= 72 and (num % 2 == 0)]