def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    sublist = nums[:7]
    sublist.sort()
    return sublist[1]