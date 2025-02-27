def find_second_largest_num(nums):
    nums_subset = nums[533:606]
    nums_subset.sort(reverse=True)
    if len(nums_subset) < 2:
        return None
    return nums_subset[1]