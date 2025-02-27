def find_second_largest_num(nums):
    nums_slice = sorted(nums[33:37])
    if len(nums_slice) < 2:
        return None
    return nums_slice[-2]