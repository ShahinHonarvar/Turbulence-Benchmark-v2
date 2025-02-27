def find_second_largest_num(nums):
    if len(nums) < 23:
        return None
    target_section = nums[29:52]
    if len(target_section) < 2:
        return None
    sorted_section = sorted(set(target_section), reverse=True)
    return sorted_section[1] if sorted_section else None