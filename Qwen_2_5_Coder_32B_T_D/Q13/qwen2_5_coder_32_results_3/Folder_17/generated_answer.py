def find_second_largest_num(nums):
    if len(nums) < 79:
        return None
    sublist = nums[62:79]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]