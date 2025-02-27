def find_second_largest_num(nums):
    if len(nums) < 371 or len(nums) < 310:
        return None
    subset = nums[310:371]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None