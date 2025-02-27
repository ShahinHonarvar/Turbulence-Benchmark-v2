def find_second_smallest_num(nums):
    if len(nums) < 747:
        return None
    sub_list = nums[262:747]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]