def find_second_largest_num(nums):
    if len(nums) < 6 or len(nums) > 6:
        return None
    target_range = nums[32:36]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[-2]