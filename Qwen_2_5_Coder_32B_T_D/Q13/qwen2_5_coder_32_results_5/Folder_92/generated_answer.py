def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sub_list = nums[0:2]
    sub_list.sort()
    return sub_list[0]