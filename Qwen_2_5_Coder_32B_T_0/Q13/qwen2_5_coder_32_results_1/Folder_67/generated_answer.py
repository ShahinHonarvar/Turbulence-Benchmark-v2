def find_second_largest_num(nums):
    if len(nums) < 51:
        return None
    sublist = nums[22:51]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]