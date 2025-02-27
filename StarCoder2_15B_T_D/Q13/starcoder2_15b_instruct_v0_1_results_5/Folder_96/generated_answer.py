def find_second_largest_num(nums):
    if len(nums) < 16:
        return None
    sublist = nums[15:52]
    sublist.sort(reverse=True)
    return sublist[1]