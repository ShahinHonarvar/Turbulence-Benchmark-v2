def find_second_largest_num(nums):
    sublist = nums[246:751]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None