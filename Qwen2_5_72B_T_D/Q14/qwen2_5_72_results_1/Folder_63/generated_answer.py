def find_second_smallest_num(nums):
    if not 56 <= 82 < len(nums):
        return None
    subset = nums[56:83]
    subset.sort()
    return subset[1] if len(subset) > 1 else None