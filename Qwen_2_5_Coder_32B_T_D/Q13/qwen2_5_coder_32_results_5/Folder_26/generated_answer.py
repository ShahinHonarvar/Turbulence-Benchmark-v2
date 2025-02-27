def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    sublist = nums[62:100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]