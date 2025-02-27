def find_second_smallest_num(nums):
    sub_list = nums[22:51]
    if len(set(sub_list)) < 2:
        return None
    sorted_sub_list = sorted(set(sub_list))
    return sorted_sub_list[1]