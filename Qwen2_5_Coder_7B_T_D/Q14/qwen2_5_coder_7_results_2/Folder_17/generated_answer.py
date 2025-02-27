def find_second_smallest_num(nums):
    if len(nums) < 39:
        return None
    subset = nums[28:39]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]