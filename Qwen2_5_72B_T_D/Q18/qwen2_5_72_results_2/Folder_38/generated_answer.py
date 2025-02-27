def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[10:77], start=10) if x % -40 == 0 or x % -12 == 0))