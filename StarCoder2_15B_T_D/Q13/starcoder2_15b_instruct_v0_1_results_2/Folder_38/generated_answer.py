def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 44:
        return sorted_nums[43]
    else:
        return None