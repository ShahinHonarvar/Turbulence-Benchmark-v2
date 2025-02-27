def find_second_largest_num(nums):
    if len(nums) < 42:
        return None
    start, end = (22, 63)
    sub_list = nums[start:end + 1]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]