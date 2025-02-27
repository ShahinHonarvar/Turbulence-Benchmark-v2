def sum_ints_div_by_either_nums(lst):
    target_range = lst[22:25]
    divisible_sum = sum((num for num in target_range if num % -85 == 0 or num % -30 == 0))
    return divisible_sum