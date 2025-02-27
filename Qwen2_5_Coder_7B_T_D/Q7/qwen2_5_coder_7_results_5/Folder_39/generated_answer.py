def all_even_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=2) if i <= 30 and num % 2 == 0]