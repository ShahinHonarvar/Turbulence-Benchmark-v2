def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 86:
        return sorted_nums[82]
    else:
        return None