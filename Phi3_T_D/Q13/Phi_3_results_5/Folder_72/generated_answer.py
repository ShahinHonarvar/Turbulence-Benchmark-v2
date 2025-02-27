def find_second_largest_num(nums):
    target_range = nums[29:52]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[-2]