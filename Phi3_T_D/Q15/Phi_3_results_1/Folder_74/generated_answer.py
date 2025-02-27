def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[16:79] if num % 2 != 0))