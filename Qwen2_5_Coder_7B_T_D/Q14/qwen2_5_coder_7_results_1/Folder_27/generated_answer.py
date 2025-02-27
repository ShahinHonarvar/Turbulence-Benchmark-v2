def find_second_smallest_num(nums):
    if len(nums) < 60:
        return None
    subset = nums[25:60]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]