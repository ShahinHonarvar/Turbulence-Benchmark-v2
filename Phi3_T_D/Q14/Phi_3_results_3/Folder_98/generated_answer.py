def find_second_smallest_num(nums):
    if len(nums) <= 1 or len(nums) < 6 + 1:
        return None
    target_range = nums[6:6 + 1]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[1]