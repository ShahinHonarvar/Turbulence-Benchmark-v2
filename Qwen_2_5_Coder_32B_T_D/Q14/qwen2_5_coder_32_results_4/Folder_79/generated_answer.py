def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sublist = nums[1:6]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None