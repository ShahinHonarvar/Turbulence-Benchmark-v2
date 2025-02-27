def find_second_largest_num(nums):
    if 22 <= len(nums) and len(nums) <= 63:
        target_range = nums[22:64]
        if len(set(target_range)) < 2:
            return None
        target_range.sort(reverse=True)
        return target_range[1]
    return None