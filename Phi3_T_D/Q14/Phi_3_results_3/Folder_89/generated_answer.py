def find_second_smallest_num(nums):
    if len(nums) < 64:
        return None
    filtered = sorted(nums[62:63])
    return filtered[0] if len(filtered) > 1 else None