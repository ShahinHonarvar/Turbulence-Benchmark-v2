def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[24:33] if num % 35 == 0 or num % 87 == 0))