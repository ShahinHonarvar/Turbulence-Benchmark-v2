def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    sub = nums[56:58]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[1]