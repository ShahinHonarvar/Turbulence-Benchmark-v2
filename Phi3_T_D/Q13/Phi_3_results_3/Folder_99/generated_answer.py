def find_second_largest_num(nums):
    if len(nums) < 41:
        return None
    sorted_items = sorted(nums[309:371])
    return sorted_items[-2] if len(sorted_items) > 1 else None