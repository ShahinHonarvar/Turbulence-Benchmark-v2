def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[10:80]) if n % -74 == 0 or n % -58 == 0))