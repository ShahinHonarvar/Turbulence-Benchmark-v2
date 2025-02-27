def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    sublist = nums[43:52]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]