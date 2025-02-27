def find_second_largest_num(nums):
    sorted_subset = sorted(nums[75:95], reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None