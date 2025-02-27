def find_second_largest_num(nums):
    if len(nums) >= 64:
        nums = nums[62:64]
    sorted_nums = sorted(nums, reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None