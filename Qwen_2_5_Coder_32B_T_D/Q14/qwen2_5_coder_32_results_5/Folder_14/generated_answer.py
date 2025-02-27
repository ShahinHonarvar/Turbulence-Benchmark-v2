def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    sub_list = nums[8:10]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]