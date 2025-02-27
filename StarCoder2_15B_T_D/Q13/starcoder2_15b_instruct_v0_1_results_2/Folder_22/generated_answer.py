def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 40:
        return sorted_nums[39]
    else:
        return None