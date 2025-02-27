def find_second_largest_num(nums):
    subset = nums[52:72]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]