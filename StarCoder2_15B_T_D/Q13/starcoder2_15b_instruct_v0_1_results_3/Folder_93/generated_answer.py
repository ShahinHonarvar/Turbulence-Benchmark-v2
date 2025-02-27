def find_second_largest_num(nums):
    if len(nums) < 95:
        return None
    sublist = nums[75:95]
    sublist.sort(reverse=True)
    return sublist[1]