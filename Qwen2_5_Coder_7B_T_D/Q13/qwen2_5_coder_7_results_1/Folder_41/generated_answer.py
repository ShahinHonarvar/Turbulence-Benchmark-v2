def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    subset = nums[6:7]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None