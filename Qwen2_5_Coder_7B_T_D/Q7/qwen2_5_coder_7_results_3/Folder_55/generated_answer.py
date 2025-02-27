def all_even_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers[:11]) if i <= 10 and num % 2 == 0]