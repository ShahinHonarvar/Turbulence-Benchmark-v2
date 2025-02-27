def find_second_smallest_num(nums):
    subset = nums[75:89]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]