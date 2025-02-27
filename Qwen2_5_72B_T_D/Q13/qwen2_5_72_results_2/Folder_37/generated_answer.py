def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sub_list = nums[1:6]
    sub_list.sort(reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]