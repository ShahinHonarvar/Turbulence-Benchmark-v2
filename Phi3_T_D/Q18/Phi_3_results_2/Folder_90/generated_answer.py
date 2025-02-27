def sum_ints_div_by_either_nums(numbers):
    sum_of_divisibles = sum((number for index, number in enumerate(numbers[138:425]) if number % -863 == 0 or number % -329 == 0))
    return sum_of_divisibles