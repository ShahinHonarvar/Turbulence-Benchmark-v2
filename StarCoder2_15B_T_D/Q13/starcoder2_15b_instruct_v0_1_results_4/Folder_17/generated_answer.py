def find_second_largest_num(nums):
    sublist = nums[62:80]
    sublist.sort(reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None