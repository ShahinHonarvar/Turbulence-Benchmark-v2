def find_second_largest_num(nums):
    if len(nums) < 200:
        return None
    start = nums[200]
    unique_nums = sorted(set(nums[200:201]), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None