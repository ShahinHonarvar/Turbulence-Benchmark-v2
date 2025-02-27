def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 24:
        return sorted_nums[23]
    else:
        return None