def find_second_largest_num(nums):
    nums_subset = nums[43:52]
    sorted_subset = sorted(nums_subset, reverse=True)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None