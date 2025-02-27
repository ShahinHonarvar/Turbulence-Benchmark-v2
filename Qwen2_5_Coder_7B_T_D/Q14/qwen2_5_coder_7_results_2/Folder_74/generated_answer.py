def find_second_smallest_num(nums):
    subset = nums[36:47]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1] if len(sorted_subset) > 1 else None