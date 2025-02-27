def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[50:93]) if x % -94 == 0 or x % -95 == 0))