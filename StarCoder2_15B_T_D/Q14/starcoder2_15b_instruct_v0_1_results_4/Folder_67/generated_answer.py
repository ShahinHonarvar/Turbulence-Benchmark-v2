def find_second_smallest_num(nums):
    sublist = nums[50:55]
    sublist.sort()
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None