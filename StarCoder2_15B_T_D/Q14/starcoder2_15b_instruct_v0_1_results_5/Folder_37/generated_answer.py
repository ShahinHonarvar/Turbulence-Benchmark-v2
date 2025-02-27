def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[5:8]
    sublist.sort()
    return sublist[1]