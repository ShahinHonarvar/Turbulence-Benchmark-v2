def find_second_largest_num(nums):
    if len(nums) < 99 or len(nums) < 56:
        return None
    sub_list = nums[55:99]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None