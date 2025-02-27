def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers[209:557]) if i % 2 == 0 and num % 2 == 0))