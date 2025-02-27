def find_second_smallest_num(nums):
    subset = nums[1:101]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1] if subset[0] != subset[1] else None