def find_second_largest_num(nums):
    start_index, end_index = (40, 80)
    if len(nums) < end_index:
        return None
    sub_list = nums[start_index:end_index + 1]
    if len(set(sub_list)) < 2:
        return None
    sub_list.remove(max(sub_list))
    return max(sub_list)