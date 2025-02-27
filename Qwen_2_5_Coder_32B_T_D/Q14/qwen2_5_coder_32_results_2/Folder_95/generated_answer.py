def find_second_smallest_num(nums):
    if len(nums) < 86:
        return None
    sub_list = nums[75:86]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]