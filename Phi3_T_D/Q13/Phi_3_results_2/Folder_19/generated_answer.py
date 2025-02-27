def find_second_largest_num(nums):
    sub_list = nums[3:6]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(set(nums))
    return sorted_list[-2] if sorted_list else None