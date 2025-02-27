def find_second_smallest_num(nums):
    temp_range_lst = nums[37:52]
    if len(temp_range_lst) < 2:
        return None
    temp_range_lst.sort()
    return temp_range_lst[1]