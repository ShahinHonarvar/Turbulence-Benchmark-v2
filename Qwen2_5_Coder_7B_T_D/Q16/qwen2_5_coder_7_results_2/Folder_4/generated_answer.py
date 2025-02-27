def sum_even_ints_inclusive(numbers):
    return sum((number for i, number in enumerate(numbers, start=1) if 12 <= i <= 92 and number % 2 == 0))