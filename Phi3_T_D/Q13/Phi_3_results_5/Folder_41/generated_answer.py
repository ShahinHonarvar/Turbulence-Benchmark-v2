def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    subset = sorted(nums[6:8], reverse=True)
    return subset[1] if len(subset) > 1 else None