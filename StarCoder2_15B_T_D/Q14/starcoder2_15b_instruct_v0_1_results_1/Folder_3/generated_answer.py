def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    sublist = nums[27:56]
    sublist.sort()
    return sublist[1]