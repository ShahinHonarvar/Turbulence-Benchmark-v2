def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[48:60]) if n % 88 == 0 or n % 58 == 0))