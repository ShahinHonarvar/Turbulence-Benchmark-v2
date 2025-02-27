def find_second_largest_num(nums):
    if len(nums) < 101 or len(set(nums[10:101])) < 2:
        return None
    sub_list = sorted(nums[10:101], reverse=True)
    return sub_list[1]