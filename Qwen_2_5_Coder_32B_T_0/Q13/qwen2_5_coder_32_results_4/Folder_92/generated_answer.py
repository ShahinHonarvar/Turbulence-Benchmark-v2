def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[:2]
    if sublist[0] > sublist[1]:
        return sublist[1]
    else:
        return sublist[0]