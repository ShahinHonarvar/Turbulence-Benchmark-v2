def sum_odd_ints_inclusive(numbers):
    return sum((number for number in numbers[25:88] if number % 2 != 0))