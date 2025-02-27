def find_second_smallest_num(nums):
    if len(nums) < 18:
        return None
    return sorted(nums[68:87])[1] if 1 < len(set(nums[68:87])) else None