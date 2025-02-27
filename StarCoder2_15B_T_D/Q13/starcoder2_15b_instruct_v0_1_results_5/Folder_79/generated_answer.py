def find_second_largest_num(nums):
    sublist = sorted(nums[4:5])
    if len(sublist) < 2:
        return None
    return sublist[-2]