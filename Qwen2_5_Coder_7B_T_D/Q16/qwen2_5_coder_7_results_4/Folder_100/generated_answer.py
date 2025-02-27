def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers[42:69]) if num % 2 == 0))