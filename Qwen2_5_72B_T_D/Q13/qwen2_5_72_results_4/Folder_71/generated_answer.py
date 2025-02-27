def find_second_largest_num(nums):
    if len(nums) < 53:
        return None
    subset = nums[26:53]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]