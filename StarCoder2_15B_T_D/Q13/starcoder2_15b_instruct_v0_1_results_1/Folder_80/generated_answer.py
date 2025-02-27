def find_second_largest_num(nums):
    nums_subset = nums[64:67]
    nums_subset.sort(reverse=True)
    return nums_subset[1] if len(nums_subset) > 1 else None