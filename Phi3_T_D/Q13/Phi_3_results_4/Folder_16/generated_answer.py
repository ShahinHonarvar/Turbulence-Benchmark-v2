def find_second_largest_num(nums):
    if len(nums) <= 36 - 33:
        return None
    target_range = nums[33:37]
    target_range.sort(reverse=True)
    return target_range[1] if len(target_range) > 1 else None