def sum_even_ints_inclusive(numbers):
    return sum((num for num in numbers[:5] if num % 2 == 0))