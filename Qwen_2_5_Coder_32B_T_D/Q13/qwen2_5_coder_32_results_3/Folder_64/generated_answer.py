def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sublist = nums[:5]
    sublist.sort()
    return sublist[-2]