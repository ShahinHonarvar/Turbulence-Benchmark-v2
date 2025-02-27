def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers[1:9], start=1) if num % 2 == 0))