def find_second_largest_num(nums):
    return max((x for i, x in enumerate(nums[22:89]) if x < max(nums[22:88])), default=None)