def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers, start=1) if 17 <= i <= 78 and num % 2 == 0))