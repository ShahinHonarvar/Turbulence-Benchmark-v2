def find_second_largest_num(nums):
    sub_list = nums[74:96]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if sub_list[0] != sub_list[1] else None