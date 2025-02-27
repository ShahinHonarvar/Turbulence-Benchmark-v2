def find_second_smallest_num(nums):
    if not 13 <= len(nums) <= 68:
        return None
    mins = sorted(set(nums[13:69]))
    return mins[1] if len(mins) > 1 else None