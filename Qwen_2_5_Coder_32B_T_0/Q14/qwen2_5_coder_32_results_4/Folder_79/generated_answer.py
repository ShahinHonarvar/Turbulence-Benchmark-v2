def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sub_list = nums[1:6]
    sub_list.sort()
    return sub_list[1]