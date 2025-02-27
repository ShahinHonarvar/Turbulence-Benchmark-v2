def find_second_largest_num(nums):
    sublist = nums[34:56]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    return None