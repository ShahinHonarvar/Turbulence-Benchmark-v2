def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sub_list = nums[62:64]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[0]