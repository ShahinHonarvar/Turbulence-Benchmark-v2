def find_second_largest_num(nums):
    sliced_list = nums[36:47]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(set(sliced_list), reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None