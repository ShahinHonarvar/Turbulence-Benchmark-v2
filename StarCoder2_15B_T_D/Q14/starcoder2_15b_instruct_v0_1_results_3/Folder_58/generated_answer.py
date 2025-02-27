def find_second_smallest_num(nums):
    sliced_list = nums[310:371]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None