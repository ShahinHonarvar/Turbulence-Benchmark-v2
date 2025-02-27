def find_second_smallest_num(nums):
    if 20 <= len(nums) <= 30:
        target_range = nums[20:31]
        if len(target_range) < 2:
            return None
        target_range.sort()
        return target_range[1]
    return None