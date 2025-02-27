def find_second_largest_num(nums):
    if len(nums) < 557 or len(nums) < 210:
        return None
    sub_list = nums[209:557]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None