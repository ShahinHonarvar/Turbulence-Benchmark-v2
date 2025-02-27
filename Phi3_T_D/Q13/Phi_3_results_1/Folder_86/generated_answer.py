def find_second_largest_num(nums):
    sliced_nums = nums[31:35]
    if len(sliced_nums) > 1:
        sliced_nums.sort()
        return sliced_nums[-2]
    return None