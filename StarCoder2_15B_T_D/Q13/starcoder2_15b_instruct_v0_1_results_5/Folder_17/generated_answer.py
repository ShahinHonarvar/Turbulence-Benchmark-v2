def find_second_largest_num(nums):
    sorted_nums = sorted(nums)
    sliced_nums = sorted_nums[62:79]
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[-2]