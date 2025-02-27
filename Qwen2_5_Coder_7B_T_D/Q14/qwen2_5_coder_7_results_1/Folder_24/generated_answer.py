def find_second_smallest_num(nums):
    if len(nums) < 24:
        return None
    subset = nums[23:24]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]