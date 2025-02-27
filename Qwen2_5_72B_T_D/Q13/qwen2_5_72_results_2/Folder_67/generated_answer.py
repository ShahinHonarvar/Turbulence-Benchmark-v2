def find_second_largest_num(nums):
    if len(nums) < 51 or len(nums) <= 22:
        return None
    sub_list = nums[22:51]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None