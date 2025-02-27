def find_second_largest_num(nums):
    if len(nums) < 25:
        return None
    sorted_nums = sorted(nums[15:40])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None