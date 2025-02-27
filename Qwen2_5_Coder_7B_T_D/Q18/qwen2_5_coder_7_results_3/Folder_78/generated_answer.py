def sum_ints_div_by_either_nums(nums):
    return sum(nums[34:70] if 34 < len(nums) < 70 else nums) if any((i % 19 == 0 or i % 32 == 0 for i in nums[34:70] if 34 < len(nums) < 70)) else 0