def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    subset = nums[12:93]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1] if len(subset) > 1 else None