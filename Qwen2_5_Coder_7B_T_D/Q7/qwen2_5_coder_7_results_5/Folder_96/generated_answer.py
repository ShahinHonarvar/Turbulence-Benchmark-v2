def all_even_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 50 and i <= 200 and (num % 2 == 0)]