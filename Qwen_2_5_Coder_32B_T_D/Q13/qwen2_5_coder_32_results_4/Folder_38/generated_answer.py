def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sublist = nums[22:64]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]