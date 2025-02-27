def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers, start=1) if 10 <= i <= 100 and num % 2 == 0))