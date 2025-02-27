def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers, start=62) if i <= 78 and num % 2 != 0))