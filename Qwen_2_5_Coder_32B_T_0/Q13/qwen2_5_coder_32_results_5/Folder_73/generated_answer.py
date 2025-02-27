def find_second_largest_num(nums):
    if len(nums) < 93:
        return None
    sublist = nums[19:93]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]