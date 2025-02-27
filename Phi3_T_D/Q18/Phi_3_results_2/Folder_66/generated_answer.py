def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[58:82] if num % 55 == 0 or num % 10 == 0))