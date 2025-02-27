def all_even_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 10 and i <= 100 and (num % 2 == 0)]