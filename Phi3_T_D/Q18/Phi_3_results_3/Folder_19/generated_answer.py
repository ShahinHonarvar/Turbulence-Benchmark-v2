def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[1:5], 1) if n % 4 == 0 or n % -6 == 0))