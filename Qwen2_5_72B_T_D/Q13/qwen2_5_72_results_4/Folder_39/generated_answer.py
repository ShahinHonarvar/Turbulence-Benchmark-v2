def find_second_largest_num(nums):
    sublist = nums[20:31]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]