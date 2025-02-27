def sum_in_range(numbers):
    total = sum((num for num in numbers if 3 <= num <= 9))
    return total