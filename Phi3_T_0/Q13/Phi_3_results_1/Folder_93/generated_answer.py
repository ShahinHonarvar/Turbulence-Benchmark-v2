def find_second_largest_num(nums):
    if len(nums) < 19:
        return None
    sorted_nums = sorted(nums[75:95])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None