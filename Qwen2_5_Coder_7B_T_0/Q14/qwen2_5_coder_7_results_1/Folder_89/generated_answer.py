def find_second_smallest_num(nums):
    if len(nums) < 64:
        return None
    sub_nums = nums[62:64]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]