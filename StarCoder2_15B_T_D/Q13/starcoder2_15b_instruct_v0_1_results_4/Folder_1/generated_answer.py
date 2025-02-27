def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[1] if len(sorted_nums) >= 32 else None