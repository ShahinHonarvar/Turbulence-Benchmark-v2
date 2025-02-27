def find_second_largest_num(nums):
    start_index, end_index = (639, 975)
    filtered_list = nums[start_index:end_index + 1]
    if len(filtered_list) < 2:
        return None
    max_num = max(filtered_list)
    filtered_list.remove(max_num)
    return max(filtered_list) if filtered_list else None