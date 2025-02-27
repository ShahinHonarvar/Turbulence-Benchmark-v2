def find_second_smallest_num(nums):
    limited_list = nums[13:69]
    if len(limited_list) < 2:
        return None
    limited_list.sort()
    return limited_list[1]