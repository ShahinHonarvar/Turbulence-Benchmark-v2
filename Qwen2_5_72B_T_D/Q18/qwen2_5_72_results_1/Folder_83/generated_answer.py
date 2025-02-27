def sum_ints_div_by_either_nums(numbers):
    return sum((number for index, number in enumerate(numbers[90:201]) if number % -31 == 0 or number % 13 == 0))