def find_second_largest_num(nums):
    if len(nums) < 13 or len(nums) > 68:
        return None
    sorted_nums = sorted(nums[12:69])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None