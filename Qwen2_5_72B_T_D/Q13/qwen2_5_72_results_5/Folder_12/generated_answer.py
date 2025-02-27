def find_second_largest_num(nums):
    if not 14 <= 64 < len(nums):
        return None
    sub_list = nums[14:65]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]