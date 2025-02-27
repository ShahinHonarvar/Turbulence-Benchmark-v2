def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 35 and i <= 64 and (num % -30 == 0) or num % -95 == 0))