def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    subset = nums[:4]
    subset.sort()
    return subset[-2] if len(subset) > 1 else None