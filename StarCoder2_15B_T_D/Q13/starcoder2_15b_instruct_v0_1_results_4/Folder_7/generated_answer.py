def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[661:925]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) >= 2 else None