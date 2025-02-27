def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i >= 22 and i <= 24 and (num % -85 == 0) or num % -30 == 0))