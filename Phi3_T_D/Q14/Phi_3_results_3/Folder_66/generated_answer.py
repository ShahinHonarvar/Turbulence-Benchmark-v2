def find_second_smallest_num(nums):
    if len(nums) < 40 or len(nums) > 40:
        return None
    target_range = nums[62:100]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[1]