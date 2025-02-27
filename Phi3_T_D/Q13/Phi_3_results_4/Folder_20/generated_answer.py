def find_second_largest_num(nums):
    sliced_list = nums[56:67]
    if len(sliced_list) < 2:
        return None
    max_val = max(sliced_list)
    sliced_list.remove(max_val)
    return max(sliced_list) if sliced_list else None