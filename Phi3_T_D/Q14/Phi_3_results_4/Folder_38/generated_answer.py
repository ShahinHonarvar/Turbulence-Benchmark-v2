def find_second_smallest_num(nums):
    sliced_list = nums[37:52]
    if len(sliced_list) >= 2:
        sorted_list = sorted(sliced_list)
        return sorted_list[1]
    return None