def find_second_largest_num(nums):
    if len(nums) < 6 or len(nums) > 6:
        return None
    sorted_nums = sorted(nums[50:55])
    return sorted_nums[-2] if len(sorted_nums) > 1 else None