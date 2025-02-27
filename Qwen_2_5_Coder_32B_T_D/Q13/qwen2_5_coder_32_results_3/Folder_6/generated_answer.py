def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    sub_list = nums[10:67]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]