def find_second_largest_num(nums):
    tail_sub_list = nums[15:40]
    if len(set(tail_sub_list)) < 2:
        return None
    return sorted(set(tail_sub_list), reverse=True)[1]