def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[:8]
    sublist.sort()
    return sublist[-2]