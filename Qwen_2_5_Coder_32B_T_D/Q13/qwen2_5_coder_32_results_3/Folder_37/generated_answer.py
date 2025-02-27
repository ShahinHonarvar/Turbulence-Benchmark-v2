def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sublist = nums[1:6]
    sublist.sort()
    return sublist[-2]