def find_second_largest_num(nums):
    if len(nums) < 976:
        return None
    sublist = nums[639:976]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]