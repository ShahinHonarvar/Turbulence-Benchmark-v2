def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    sublist = nums[:3]
    sublist.sort()
    return sublist[1]