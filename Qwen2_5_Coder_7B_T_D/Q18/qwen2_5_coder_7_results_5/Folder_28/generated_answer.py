def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[34:82] if num % 27 == 0 or num % 57 == 0))