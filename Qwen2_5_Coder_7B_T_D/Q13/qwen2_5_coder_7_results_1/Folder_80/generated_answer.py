def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    subset = nums[64:67]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset))[-2]