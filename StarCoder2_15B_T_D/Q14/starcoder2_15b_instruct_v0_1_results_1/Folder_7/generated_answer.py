def find_second_smallest_num(nums):
    nums_subset = nums[686:988]
    sorted_subset = sorted(nums_subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]