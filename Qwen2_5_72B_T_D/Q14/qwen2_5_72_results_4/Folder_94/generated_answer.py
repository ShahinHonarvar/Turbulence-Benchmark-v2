def find_second_smallest_num(nums):
    if len(nums) < 72:
        return None
    subset = nums[52:72]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]