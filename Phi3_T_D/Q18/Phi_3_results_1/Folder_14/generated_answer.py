def sum_ints_div_by_either_nums(numbers):
    target_nums = numbers[7:10]
    return sum((num for num in target_nums if num % 2 == 0 or num % 3 == 0))