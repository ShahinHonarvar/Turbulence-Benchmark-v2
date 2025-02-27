def find_second_largest_num(nums):
    sublist = nums[43:52]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]