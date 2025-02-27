def sum_ints_div_by_either_nums(nums):
    total = sum((x for x in nums[29:46] if x % 27 == 0 or x % 81 == 0))
    return total