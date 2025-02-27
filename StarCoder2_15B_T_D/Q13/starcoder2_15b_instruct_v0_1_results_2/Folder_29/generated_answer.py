def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    sliced_nums = sorted_nums[59:98]
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]