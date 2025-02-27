def find_second_largest_num(nums):
    if len(nums) < 31:
        return None
    subset = nums[20:31]
    subset.remove(max(subset))
    return max(subset) if subset else None