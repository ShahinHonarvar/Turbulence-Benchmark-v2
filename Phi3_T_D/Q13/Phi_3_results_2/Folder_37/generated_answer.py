def find_second_largest_num(nums):
    sliced_list = nums[1:6]
    if len(sliced_list) == 0:
        return None
    sorted_list = sorted(sliced_list, reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None