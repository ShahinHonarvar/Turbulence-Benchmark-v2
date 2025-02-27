def find_second_largest_num(nums):
    sublist = sorted(nums[209:557], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]