def find_second_smallest_num(nums):
    if len(nums) < 78 or len(nums) < 17:
        return None
    sub_list = nums[17:79]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None