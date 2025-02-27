def find_second_largest_num(nums):
    sliced_list = nums[75:89]
    if len(sliced_list) < 2:
        return None
    return sorted(sliced_list)[-2]