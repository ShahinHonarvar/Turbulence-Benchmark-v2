def find_second_smallest_num(nums):
    subset = nums[40:201]
    if len(subset) < 2:
        return None
    subset.remove(min(subset))
    return min(subset)