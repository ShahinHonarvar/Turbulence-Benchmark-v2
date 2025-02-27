def find_second_largest_num(nums):
    if len(nums) < 36:
        return None
    sublist = nums[32:36]
    sublist.sort(reverse=True)
    return sublist[1]