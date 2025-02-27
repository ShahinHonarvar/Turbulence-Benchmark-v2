def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    unique_nums = sorted(set(nums[:8]), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None