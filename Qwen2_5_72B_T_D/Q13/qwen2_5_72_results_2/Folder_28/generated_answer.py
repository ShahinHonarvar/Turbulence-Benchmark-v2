def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    subset = nums[62:64]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[1]