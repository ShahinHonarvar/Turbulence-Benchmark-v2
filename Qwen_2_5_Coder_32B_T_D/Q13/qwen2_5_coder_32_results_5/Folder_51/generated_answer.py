def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_list = nums[1:9]
    sub_list.sort()
    return sub_list[-2]