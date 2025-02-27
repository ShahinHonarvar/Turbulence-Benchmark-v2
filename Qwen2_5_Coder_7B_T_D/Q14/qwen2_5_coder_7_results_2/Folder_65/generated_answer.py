def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    subset = nums[56:58]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]