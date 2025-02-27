def find_second_largest_num(nums):
    if len(nums) < 24:
        return None
    sub = nums[23:24]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[-2]