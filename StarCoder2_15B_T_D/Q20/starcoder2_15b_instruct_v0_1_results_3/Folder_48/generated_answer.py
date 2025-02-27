def find_n_th_smallest_num(nums):
    sublist = nums[127:849]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 10:
        return sorted_sublist[9]
    else:
        return None