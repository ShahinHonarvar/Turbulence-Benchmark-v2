def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[154:799]) if num % 275 == 0 or num % 580 == 0))