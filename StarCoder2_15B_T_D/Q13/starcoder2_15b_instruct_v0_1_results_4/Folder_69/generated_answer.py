def find_second_largest_num(nums):
    sorted_sublist = sorted(nums[32:36], reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]