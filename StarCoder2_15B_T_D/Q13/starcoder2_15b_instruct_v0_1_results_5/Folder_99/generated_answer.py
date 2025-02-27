def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 311:
        return sorted_nums[310]
    else:
        return None