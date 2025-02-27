def sum_ints_div_by_either_nums(lst):
    target_range = lst[7:10]
    divisible_nums = [num for num in target_range if num % -9 == 0 or num % -7 == 0]
    return sum(divisible_nums)