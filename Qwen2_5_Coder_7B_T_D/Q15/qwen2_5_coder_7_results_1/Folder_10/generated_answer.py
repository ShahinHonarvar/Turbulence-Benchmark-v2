def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[25:60] if num % 2 != 0))