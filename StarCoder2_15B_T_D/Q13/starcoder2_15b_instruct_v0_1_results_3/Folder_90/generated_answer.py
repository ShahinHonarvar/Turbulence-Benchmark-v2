def find_second_largest_num(nums):
    sublist = nums[262:747]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None