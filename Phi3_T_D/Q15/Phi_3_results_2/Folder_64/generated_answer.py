def sum_odd_ints_inclusive(numbers):
    return sum((number for number in numbers[0:5] if number % 2 != 0))