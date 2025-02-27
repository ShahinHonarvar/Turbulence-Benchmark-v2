def find_second_largest_num(nums):
    if len(nums) < 4 or len(nums) > 4:
        return None
    sorted_nums = sorted(nums[33:37])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None