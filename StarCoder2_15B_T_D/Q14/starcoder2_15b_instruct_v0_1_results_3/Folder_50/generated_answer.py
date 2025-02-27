def find_second_smallest_num(nums):
    sublist = nums[42:70]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None