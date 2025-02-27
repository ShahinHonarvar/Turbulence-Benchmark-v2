def sum_odd_ints_inclusive(numbers):
    return sum((number for number in numbers[310:371] if number % 2 == 1))