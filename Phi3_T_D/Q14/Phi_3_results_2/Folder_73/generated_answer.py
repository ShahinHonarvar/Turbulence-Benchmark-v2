def find_second_smallest_num(nums):
    sliced_list = nums[59:98]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]