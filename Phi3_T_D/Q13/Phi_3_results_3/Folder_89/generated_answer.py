def find_second_largest_num(nums):
    if len(nums) <= 82:
        return None
    sublist = nums[56:83]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]