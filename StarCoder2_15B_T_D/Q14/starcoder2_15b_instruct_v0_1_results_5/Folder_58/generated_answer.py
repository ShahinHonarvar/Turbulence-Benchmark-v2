def find_second_smallest_num(nums):
    if len(nums) < 371:
        return None
    sublist = nums[310:371]
    sublist.sort()
    return sublist[1]