def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    sliced_nums = sorted_nums[52:72]
    if not sliced_nums:
        return None
    return sliced_nums[1]