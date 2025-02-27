def find_second_smallest_num(nums):
    sublist = nums[75:86]
    if len(sublist) < 2:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    second_min_num = min(sublist)
    return second_min_num