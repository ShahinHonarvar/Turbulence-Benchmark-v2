def find_second_largest_num(nums):
    subset = nums[246:751]
    sorted_subset = sorted(subset, reverse=True)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None