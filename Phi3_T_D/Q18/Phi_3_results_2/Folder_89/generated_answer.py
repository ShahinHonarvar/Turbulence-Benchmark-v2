def sum_ints_div_by_either_nums(numbers):
    return sum((number for number in numbers[28:97] if number % 90 == 0 or number % 97 == 0))