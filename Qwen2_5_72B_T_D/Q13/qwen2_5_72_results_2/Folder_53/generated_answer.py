def find_second_largest_num(nums):
    sub_list = nums[100:201]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    second_max = max(sub_list) if sub_list else None
    return second_max