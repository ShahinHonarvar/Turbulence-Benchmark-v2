def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums[51:77]) if n % -90 == 0 or n % -59 == 0))