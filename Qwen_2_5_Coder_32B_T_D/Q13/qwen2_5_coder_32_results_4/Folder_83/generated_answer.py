def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    sub_list = nums[90:91]
    return None if len(sub_list) < 2 else sorted(sub_list)[-2]