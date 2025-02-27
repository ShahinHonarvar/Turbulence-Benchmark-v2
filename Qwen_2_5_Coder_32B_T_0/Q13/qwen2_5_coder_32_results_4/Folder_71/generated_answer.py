def find_second_largest_num(nums):
    if len(nums) < 53:
        return None
    sublist = nums[26:53]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]