def find_second_smallest_num(nums):
    sorted_sublist = sorted(nums[29:52])
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None