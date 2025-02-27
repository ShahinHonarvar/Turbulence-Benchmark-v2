def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sub_nums = nums[3:6]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]