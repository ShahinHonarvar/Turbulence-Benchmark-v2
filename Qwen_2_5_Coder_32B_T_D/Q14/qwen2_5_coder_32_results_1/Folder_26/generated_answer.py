def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    sub = nums[62:79]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[1]