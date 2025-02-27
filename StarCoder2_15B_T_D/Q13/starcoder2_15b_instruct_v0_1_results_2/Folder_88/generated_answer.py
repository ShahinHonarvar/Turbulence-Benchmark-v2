def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[4:9]
    sublist.sort(reverse=True)
    return sublist[1]