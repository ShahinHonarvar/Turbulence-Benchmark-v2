def find_second_largest_num(nums):
    trimmed_list = nums[40:201]
    if len(trimmed_list) < 2:
        return None
    max_num = max(trimmed_list)
    trimmed_list.remove(max_num)
    return max(trimmed_list)