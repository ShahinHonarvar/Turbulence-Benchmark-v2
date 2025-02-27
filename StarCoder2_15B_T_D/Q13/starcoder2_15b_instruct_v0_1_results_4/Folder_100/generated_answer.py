def find_second_largest_num(nums):
    sublist = nums[42:69]
    sublist.sort(reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None