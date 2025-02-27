def find_second_smallest_num(nums):
    sublist = sorted(nums[32:36])
    return sublist[1] if len(sublist) == 4 else None