def find_second_largest_num(nums):
    if 26 <= len(nums) <= 52:
        unique_nums = sorted(set(nums[26:53]), reverse=True)
        return unique_nums[1] if len(unique_nums) > 1 else None
    return None