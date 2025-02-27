def sum_ints_div_by_either_nums(numbers):
    return sum((number for number in numbers[40:201] if number % 21 == 0 or number % 71 == 0))