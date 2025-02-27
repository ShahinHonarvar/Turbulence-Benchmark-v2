def find_second_largest_num(nums):
    nums_subset = nums[37:52]
    nums_subset.sort(reverse=True)
    if len(nums_subset) >= 2:
        return nums_subset[1]
    else:
        return None