def find_second_largest_num(nums):
    if len(nums) <= 51:
        return None
    subset = nums[37:52]
    subset.sort()
    if len(subset) <= 1:
        return None
    return subset[-2]