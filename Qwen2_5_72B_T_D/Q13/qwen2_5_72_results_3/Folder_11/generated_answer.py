def find_second_largest_num(nums):
    subset = nums[37:52]
    if len(subset) < 2:
        return None
    subset.remove(max(subset))
    return max(subset)