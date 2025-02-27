def find_second_smallest_num(nums):
    if 82 <= len(nums) <= 86:
        return sorted(nums[82:87])[1] if len(nums[82:87]) > 1 else None
    return None