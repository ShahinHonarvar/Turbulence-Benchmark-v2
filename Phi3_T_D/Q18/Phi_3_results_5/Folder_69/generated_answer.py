def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[61:89] if n % 31 == 0 or n % 11 == 0))