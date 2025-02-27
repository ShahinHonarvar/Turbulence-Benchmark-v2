def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sliced_nums = nums[5:8]
    if len(sliced_nums) < 2:
        return None
    sliced_nums.sort()
    return sliced_nums[-2]