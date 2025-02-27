def find_second_smallest_num(nums):
    if len(nums) < 72:
        return None
    sublist = nums[52:72]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]