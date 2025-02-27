def find_second_smallest_num(nums):
    if len(nums) < 49:
        return None
    sub_list = nums[30:49]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None