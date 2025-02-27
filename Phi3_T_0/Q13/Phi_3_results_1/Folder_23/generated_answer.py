def find_second_largest_num(nums):
    if len(nums) < 20:
        return None
    sorted_nums = sorted(nums[52:72])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None