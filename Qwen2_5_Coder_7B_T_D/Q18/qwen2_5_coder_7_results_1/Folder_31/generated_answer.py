def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[56:89]) if x % -59 == 0 or x % -79 == 0))