def find_second_smallest_num(nums):
    if len(nums) < 83:
        return None
    sub_list = nums[56:83]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]