def find_second_largest_num(nums):
    sub_list = nums[533:606]
    if len(sub_list) < 2 or max(sub_list) >= sub_list[sub_list.index(max(sub_list)) - 1]:
        return None
    return sorted(sub_list)[-2]