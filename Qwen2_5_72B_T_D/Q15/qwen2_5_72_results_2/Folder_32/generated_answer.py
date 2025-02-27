def sum_odd_ints_inclusive(numbers):
    return sum((number for number in numbers[21:98] if number % 2 != 0))