def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[10:46 + 1], start=11) if n % 55 == 0 or n % 36 == 0))