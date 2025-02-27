def find_second_largest_num(nums):
    if len(nums[1:6]) < 2:
        return None
    sorted_section = sorted(nums[1:6], reverse=True)
    return sorted_section[1] if sorted_section[0] != sorted_section[1] else None