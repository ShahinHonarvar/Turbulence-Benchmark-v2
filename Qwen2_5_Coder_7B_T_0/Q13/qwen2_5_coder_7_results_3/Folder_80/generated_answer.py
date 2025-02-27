def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    sub_nums = nums[64:67]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]