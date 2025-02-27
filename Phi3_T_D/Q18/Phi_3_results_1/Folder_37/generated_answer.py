def sum_ints_div_by_either_nums(nums):
    return sum((val for i, val in enumerate(nums[2:8], 2) if val % -1 == 0 or val % -7 == 0))