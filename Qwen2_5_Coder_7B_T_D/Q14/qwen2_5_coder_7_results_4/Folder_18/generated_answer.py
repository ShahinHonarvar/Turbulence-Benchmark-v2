def find_second_smallest_num(nums):
    subset = nums[30:49]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]