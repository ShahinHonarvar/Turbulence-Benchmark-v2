def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_list = nums[4:9]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]