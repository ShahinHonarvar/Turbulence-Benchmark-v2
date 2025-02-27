def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 30:
        return None
    sliced_nums = sorted_nums[30:88]
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[-2]