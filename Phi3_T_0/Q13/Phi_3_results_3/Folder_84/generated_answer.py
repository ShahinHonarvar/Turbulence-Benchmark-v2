def find_second_largest_num(nums):
    if len(nums) < 44:
        return None
    sub_list = nums[43:87]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]