def find_second_largest_num(nums):
    sub_nums = nums[75:86]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[-2]