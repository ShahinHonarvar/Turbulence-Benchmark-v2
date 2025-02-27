def find_second_largest_num(nums):
    if len(nums) < 91:
        return None
    sublist = nums[90:91]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]