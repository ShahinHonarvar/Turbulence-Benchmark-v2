def find_second_largest_num(nums):
    sublist = nums[56:100]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]