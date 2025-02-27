def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[10:29]) if n % -61 == 0 or n % -64 == 0))