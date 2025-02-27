def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[38:82]) if x % -61 == 0 or x % -71 == 0))