def find_second_largest_num(nums):
    if len(nums) < 12 or len(nums) > 92:
        return None
    sorted_nums = sorted(nums[11:93])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None