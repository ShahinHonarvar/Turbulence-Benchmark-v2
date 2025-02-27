def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[69:71] if x % 72 == 0 or x % 70 == 0)) if len(nums) > 70 else 0