def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[50:201], start=50) if x % -34 == 0 or x % 64 == 0))