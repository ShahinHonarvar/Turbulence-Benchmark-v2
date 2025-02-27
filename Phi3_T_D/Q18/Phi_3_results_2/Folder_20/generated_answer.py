def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[48:77]) if x % -46 == 0 or x % -82 == 0))