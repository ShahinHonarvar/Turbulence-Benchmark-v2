def find_second_largest_num(nums):
    if not 20 <= len(nums) >= 200:
        return None
    subset = nums[20:201]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset) if subset else None