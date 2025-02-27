def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    sub_nums = nums[6:7]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[-2]