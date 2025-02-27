def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    sublist = nums[:7]
    sublist.sort()
    return sublist[-2]