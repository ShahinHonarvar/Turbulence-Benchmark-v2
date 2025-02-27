def find_second_largest_num(nums):
    if len(nums) <= 6:
        return None
    subset = nums[6:7]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]