def find_second_smallest_num(nums):
    if len(nums) < 60:
        return None
    sub_list = nums[25:60]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]