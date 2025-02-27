def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 100:
        return sorted_nums[98]
    else:
        return None