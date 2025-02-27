def find_second_largest_num(nums):
    sliced_list = nums[29:80]
    sorted_list = sorted(sliced_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]