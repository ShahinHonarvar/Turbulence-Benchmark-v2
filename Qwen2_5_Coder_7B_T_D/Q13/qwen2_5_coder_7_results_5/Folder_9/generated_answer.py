def find_second_largest_num(nums):
    if len(nums) < 401:
        return None
    sub_nums = nums[200:201]
    if len(sub_nums) == 0:
        return None
    return None