def find_second_largest_num(nums):
    if len(nums) < 98 or 21 > 97:
        return None
    sublist = nums[21:98]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]