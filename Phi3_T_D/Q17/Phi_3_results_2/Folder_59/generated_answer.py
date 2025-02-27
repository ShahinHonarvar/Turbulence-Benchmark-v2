def all_ints_div_by_both_two_nums(numbers):
    return [num for num in numbers[0:9] if num % -3 == 0 and num % 8 == 0]