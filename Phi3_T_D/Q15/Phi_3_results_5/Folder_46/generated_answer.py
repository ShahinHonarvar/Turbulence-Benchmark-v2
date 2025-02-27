def sum_odd_ints_inclusive(numbers):
    start, end = (30, 87)
    return sum((num for i, num in enumerate(numbers[start:end + 1], start) if num % 2 != 0))