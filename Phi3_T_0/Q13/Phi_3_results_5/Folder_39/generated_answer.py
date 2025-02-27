def find_second_largest_num(nums):
    if len(nums) < 11 or len(nums) > 11:
        return None
    sorted_nums = sorted(nums[20:31])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None