def find_second_smallest_num(nums):
    nums_subset = nums[30:201]
    nums_subset.sort()
    if len(nums_subset) < 2:
        return None
    else:
        return nums_subset[1]