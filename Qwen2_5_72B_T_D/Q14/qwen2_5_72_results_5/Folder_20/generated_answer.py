def find_second_smallest_num(nums):
    if len(nums) < 95:
        return None
    subset = nums[75:95]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[1]