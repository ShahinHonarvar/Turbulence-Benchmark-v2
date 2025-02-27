def find_second_largest_num(nums):
    if len(nums) < 976:
        return None
    sub_list = nums[639:976]
    if len(set(sub_list)) < 2:
        return None
    return sorted(set(sub_list), reverse=True)[1]