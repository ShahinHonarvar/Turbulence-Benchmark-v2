def find_second_smallest_num(nums):
    if len(nums) < 21:
        return None
    subset = nums[10:21]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]