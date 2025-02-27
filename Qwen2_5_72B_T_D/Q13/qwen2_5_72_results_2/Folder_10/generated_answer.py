def find_second_largest_num(nums):
    sublist = nums[25:60]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max = max(sublist) if sublist else None
    return second_max