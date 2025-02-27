def find_second_largest_num(nums):
    sliced_nums = nums[16:62]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(sliced_nums, reverse=True)
    return sorted_nums[1]