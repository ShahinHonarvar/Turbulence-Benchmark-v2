def find_second_largest_num(nums):
    if len(nums) < 925 or 661 > 924:
        return None
    sub_list = nums[661:925]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]