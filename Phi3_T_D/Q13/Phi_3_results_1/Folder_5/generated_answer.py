def find_second_largest_num(nums):
    sliced_list = nums[8:10]
    if not sliced_list or len(set(sliced_list)) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]