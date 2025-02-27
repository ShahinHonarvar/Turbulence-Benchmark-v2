def find_second_smallest_num(nums):
    sub_list = sorted(nums[25:88])
    if len(sub_list) > 1:
        return sub_list[1]
    return None