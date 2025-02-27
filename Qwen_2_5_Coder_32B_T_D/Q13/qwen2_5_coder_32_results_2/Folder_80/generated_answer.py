def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    sub_list = nums[64:67]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[-2]