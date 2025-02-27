def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[28:97]) if n % 90 == 0 or n % 97 == 0))