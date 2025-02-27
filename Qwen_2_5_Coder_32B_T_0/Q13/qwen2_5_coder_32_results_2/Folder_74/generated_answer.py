def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    sublist = nums[17:79]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]