def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[34:82] if x % 27 == 0 or x % 57 == 0))