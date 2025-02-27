def find_second_smallest_num(nums):
    if len(nums) < 24:
        return None
    sub_nums = nums[23:24]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]