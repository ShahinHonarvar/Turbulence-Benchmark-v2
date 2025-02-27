def find_second_largest_num(nums):
    if len(nums) < 28:
        return None
    start, end = (66, 93)
    sub_list = nums[start:end + 1]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]