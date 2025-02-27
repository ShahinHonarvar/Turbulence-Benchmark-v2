def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers[:7]) if num % 2 == 0))