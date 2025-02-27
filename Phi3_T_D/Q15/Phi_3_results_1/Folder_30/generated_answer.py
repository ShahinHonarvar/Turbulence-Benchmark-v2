def sum_odd_ints_inclusive(numbers):
    return sum((num for idx, num in enumerate(numbers[55:99], start=55) if num % 2 != 0))