def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[68:99 + 1]) if n % -37 == 0 or n % -26 == 0))