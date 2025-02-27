def find_second_largest_num(nums):
    if len(nums) < 62:
        return None
    sublist = nums[16:62]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]