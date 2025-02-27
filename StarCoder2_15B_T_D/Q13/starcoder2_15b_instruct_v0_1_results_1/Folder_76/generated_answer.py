def find_second_largest_num(nums):
    subset = sorted(nums[686:988])
    if len(subset) < 2:
        return None
    return subset[-2]