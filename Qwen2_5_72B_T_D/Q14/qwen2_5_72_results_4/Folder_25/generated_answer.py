def find_second_smallest_num(nums):
    if len(nums) < 77 or len(nums) < 38:
        return None
    sub_list = nums[37:77]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]