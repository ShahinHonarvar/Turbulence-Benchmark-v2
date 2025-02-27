def sum_ints_div_by_either_nums(numbers):
    return sum((number for number in numbers[80:201] if number % 10 == 0 or number % 1000 == 0))