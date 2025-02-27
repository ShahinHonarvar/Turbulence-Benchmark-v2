def find_second_largest_num(nums):
    if len(nums) < 371:
        return None
    sub_list = nums[310:371]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]