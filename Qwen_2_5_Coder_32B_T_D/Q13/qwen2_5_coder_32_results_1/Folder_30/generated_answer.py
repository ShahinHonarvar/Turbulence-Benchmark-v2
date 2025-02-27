def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sublist = nums[55:99]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]