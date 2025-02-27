def sum_ints_div_by_either_nums(nums):
    total = sum((n for n in nums[30:201] if n % 115 == 0 or n % -115 == 0))
    return total