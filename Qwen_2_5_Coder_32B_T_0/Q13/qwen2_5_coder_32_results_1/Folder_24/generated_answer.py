def find_second_largest_num(nums):
    if len(nums) < 96:
        return None
    sub_list = nums[74:96]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]