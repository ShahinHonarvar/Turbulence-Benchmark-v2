def find_second_largest_num(nums):
    if len(nums) < 93 or not nums[19:93]:
        return None
    sliced_nums = nums[19:93]
    sliced_nums.sort()
    return sliced_nums[-2]