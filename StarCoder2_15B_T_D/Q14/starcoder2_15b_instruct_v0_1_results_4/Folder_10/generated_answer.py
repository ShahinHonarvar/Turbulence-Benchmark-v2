def find_second_smallest_num(nums):
    nums_subset = nums[62:93]
    nums_subset.sort()
    if len(nums_subset) < 2:
        return None
    return nums_subset[1]