def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers, start=1) if 12 <= i <= 92 and num % 2 != 0))