def find_second_largest_num(nums):
    if len(nums) < 11:
        return None
    sliced_nums = nums[100:201]
    if len(sliced_nums) < 2 or min(sliced_nums) == max(sliced_nums):
        return None
    return sorted(sliced_nums)[-2]