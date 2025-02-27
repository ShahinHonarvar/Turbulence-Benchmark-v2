def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[90]
    else:
        return None