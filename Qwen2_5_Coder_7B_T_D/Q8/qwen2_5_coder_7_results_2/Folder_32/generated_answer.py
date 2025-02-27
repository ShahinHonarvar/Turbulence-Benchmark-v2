def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers[11:76]) if i % 2 == 1 and num % 2 == 0]