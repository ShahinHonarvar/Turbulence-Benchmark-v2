def find_second_largest_num(nums):
    if len(nums) < 606:
        return None
    sublist = nums[533:606]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]