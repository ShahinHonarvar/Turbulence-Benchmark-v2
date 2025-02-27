def find_second_largest_num(nums):
    if len(nums) < 58:
        return None
    sub_nums = nums[56:58]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort(reverse=True)
    return sub_nums[1]