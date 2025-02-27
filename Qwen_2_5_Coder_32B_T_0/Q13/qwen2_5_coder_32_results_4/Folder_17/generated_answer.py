def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    sub_list = nums[62:79]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]