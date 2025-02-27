def find_second_largest_num(nums):
    sub_list = nums[62:79]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list, reverse=True)
    return sorted_sub_list[1] if sorted_sub_list[0] != sorted_sub_list[1] else None