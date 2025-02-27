def find_second_largest_num(nums):
    subset = nums[34:56]
    subset.sort()
    if len(subset) < 2:
        return None
    return subset[-2]