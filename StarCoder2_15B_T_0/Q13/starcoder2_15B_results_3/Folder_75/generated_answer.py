def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 58:
        return sorted_nums[57]
    else:
        return None