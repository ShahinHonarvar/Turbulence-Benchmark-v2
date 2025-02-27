def find_second_largest_num(nums):
    if len(nums) < 39:
        return None
    sub = nums[28:39]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[-2]