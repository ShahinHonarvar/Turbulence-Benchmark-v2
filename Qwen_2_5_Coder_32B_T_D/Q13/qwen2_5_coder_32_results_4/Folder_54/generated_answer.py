def find_second_largest_num(nums):
    if len(nums) < 56 or not nums[34:56]:
        return None
    sub_list = nums[34:56]
    sub_list.sort()
    return sub_list[-2]