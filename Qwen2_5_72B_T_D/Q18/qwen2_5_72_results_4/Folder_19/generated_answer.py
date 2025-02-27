def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[1:5] if num % 4 == 0 or num % -6 == 0))