def find_second_largest_num(nums):
    if len(nums) < 747:
        return None
    sublist = nums[262:747]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]