def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    subset = nums[62:100]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]