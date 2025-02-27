def find_second_largest_num(nums):
    if len(nums) < 6 or len(nums) > 33:
        return None
    target_range = nums[28:33]
    if len(set(target_range)) < 2:
        return None
    return sorted(set(target_range))[-2]