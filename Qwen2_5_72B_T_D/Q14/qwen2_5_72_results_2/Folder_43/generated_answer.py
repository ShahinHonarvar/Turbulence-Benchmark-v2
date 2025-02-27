def find_second_smallest_num(nums):
    if len(nums) < 96 or len(set(nums[74:96])) < 2:
        return None
    sub_list = nums[74:96]
    sub_list.sort()
    return sub_list[1]