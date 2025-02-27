def find_second_largest_num(nums):
    if len(nums) < 65:
        return None
    sublist = nums[14:65]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]