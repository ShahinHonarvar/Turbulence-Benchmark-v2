def find_second_largest_num(nums):
    if len(nums) < 11:
        return None
    sublist = nums[:11]
    sublist.sort()
    return sublist[-2]