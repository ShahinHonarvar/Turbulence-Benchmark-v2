def find_second_smallest_num(nums):
    sublist = nums[29:94]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]