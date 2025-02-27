def find_second_largest_num(nums):
    start_idx = 527
    end_idx = 538
    sublist = nums[start_idx:end_idx + 1]
    sublist.sort(reverse=True)
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None