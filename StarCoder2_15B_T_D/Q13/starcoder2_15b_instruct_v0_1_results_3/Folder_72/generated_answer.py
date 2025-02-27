def find_second_largest_num(nums):
    sublist = sorted(nums[29:52], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]