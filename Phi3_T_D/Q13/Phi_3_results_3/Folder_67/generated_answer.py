def find_second_largest_num(nums):
    sliced = nums[22:51]
    if len(sliced) < 2:
        return None
    sliced.sort()
    return sliced[-2]