def find_second_largest_num(nums):
    if len(nums) < 56:
        return None
    sub_list = nums[34:56]
    if len(sub_list) < 2:
        return None
    sub_list.remove(max(sub_list))
    return max(sub_list)