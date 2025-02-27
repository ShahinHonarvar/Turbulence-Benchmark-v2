def find_second_smallest_num(nums):
    if len(nums) < 11 or len(nums) > 12:
        return None
    start, end = (56, 66)
    sub_list = nums[start:end + 1]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]