def find_second_largest_num(nums):
    if len(nums) < 33:
        return None
    subset = nums[28:33]
    subset.remove(max(subset))
    return max(subset) if subset else None