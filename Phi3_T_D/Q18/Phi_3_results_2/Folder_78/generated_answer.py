def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[34:69 + 1] if n % 19 == 0 or n % 32 == 0))