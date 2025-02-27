def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    sublist = nums[90:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]