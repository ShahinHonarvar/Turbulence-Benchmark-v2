def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[:2]
    sublist.sort()
    return sublist[0] if len(sublist) > 1 else None