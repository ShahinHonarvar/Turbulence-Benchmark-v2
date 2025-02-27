def find_second_largest_num(nums):
    if len(nums) < 95:
        return None
    sub_list = nums[75:95]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]