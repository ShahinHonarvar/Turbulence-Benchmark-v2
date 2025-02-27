def find_second_largest_num(nums):
    sub_nums = nums[52:72]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(sub_nums, reverse=True)
    return sorted_nums[1]