def find_second_smallest_num(nums):
    if len(nums) <= 23:
        return None
    sublist = nums[23:24]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1] if len(sorted(sublist)) > 1 else None