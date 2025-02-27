def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    range_to_check = nums[6:13]
    if len(range_to_check) == 0:
        return None
    sorted_range = sorted(range_to_check, reverse=True)
    return sorted_range[1] if len(sorted_range) > 1 else None