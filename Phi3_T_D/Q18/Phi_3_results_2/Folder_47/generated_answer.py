def sum_ints_div_by_either_nums(nums):
    total = sum((n for i, n in enumerate(nums[42:88]) if n % -90 == 0 or n % -74 == 0))
    return total