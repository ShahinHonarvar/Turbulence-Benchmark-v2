def find_second_largest_num(nums):
    start_index, end_index = (56, 57)
    sub_list = nums[start_index:end_index + 1]
    if len(sub_list) < 2 or max(sub_list) == min(sub_list):
        return None
    sub_list.remove(max(sub_list))
    return max(sub_list)