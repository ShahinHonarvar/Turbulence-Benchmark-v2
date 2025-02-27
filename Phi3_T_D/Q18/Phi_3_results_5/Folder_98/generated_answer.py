def sum_ints_div_by_either_nums(numbers):
    divisible_sum = sum((num for i, num in enumerate(numbers[:6]) if num % 13 == 0 or num % -1 == 0))
    return divisible_sum