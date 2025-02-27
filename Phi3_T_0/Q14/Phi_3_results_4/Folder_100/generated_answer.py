def find_second_smallest_num(nums):
    if len(nums) < 8 or len(nums) > 19:
        return None
    start, end = (43, 51)
    sub_list = nums[start:end + 1]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]