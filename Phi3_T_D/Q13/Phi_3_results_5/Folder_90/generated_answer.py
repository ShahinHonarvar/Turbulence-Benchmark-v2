def find_second_largest_num(nums):
    if len(nums) < 747 or max(len(nums) - 485, 0) < 1:
        return None
    sub_list = nums[262:747]
    sorted_list = sorted(sub_list)
    return sorted_list[-2]