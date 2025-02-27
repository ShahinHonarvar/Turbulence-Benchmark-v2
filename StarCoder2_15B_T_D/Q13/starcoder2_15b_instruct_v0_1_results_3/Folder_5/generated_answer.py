def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    sublist = nums[8:10]
    sublist.sort(reverse=True)
    return sublist[1]