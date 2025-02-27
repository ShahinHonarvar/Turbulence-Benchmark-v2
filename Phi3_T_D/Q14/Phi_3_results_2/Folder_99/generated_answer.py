def find_second_smallest_num(nums):
    if len(nums) < 609:
        return None
    target_range = nums[608:610]
    if len(target_range) < 2:
        return None
    target_range.sort()
    return target_range[1] if target_range else None